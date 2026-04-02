# Alterações Necessárias - HelpClinic

## 📋 Resumo das Alterações Detectadas

### ✅ ALTERAÇÕES JÁ REALIZADAS (Git Diff)

#### 1. **login/cadastrar.py** - Correção de hash bcrypt
- **Mudança**: Armazenar hash bcrypt como string
- **Antes**: `cursor.execute(..., (self.user, senha_criptografada))`
  - Tentava armazenar bytes diretamente (errado)
- **Depois**: Converte para UTF-8 string antes de armazenar
- **Motivo**: bcrypt.hashpw() retorna bytes, não string

#### 2. **login/validação.py** - Correção no hash comparison
- **Mudança**: Tratamento robusto do hash ao comparar
- **Antes**: `hash_db.encode('utf-8')` (assumia ser string sempre)
- **Depois**: Verifica tipo e converte se necessário
- **Motivo**: Garantir compatibilidade se o hash for armazenado de formas diferentes

#### 3. **routes.py** - Correção de timestamps JWT
- **Mudança**: Usar Unix timestamps em vez de objetos datetime
- **Antes**: Armazenava datetime objects diretamente em JWT
- **Depois**: Usa `.timestamp()` para converter em números Unix
- **Motivo**: JWT requer timestamps numéricos, não objetos

#### 4. **routes.py** - Fix de consistência no cadastro
- **Mudança**: Campo do formulário de 'usuário' para 'email'
- **Antes**: `request.form.get('usuário')`
- **Depois**: `request.form.get('email')`
- **Motivo**: Consistência com o resto do código

---

## ⚠️ ISSUES A SEREM CORRIGIDAS

### 🔴 CRÍTICAS

#### 1. **Error Handling Genérico**
**Arquivo**: `routes.py` (linhas 111-116, 118)
```python
except:
    print("ERRO: Cadastro não realizado.")
```
**Problema**: Usa `except:` amplo demais
**Solução**: Especificar exceções:
```python
except ValueError as e:
    flash(f"Erro: {e}")
except Exception as e:
    flash(f"Erro ao cadastrar: {e}")
```

#### 2. **Segurança SSL/TLS**
**Arquivo**: `routes.py` (linha 93)
```python
response.set_cookie('auth_token', token, ..., secure=False)
```
**Problema**: `secure=False` permite cookie em HTTP (inseguro)
**Solução**: Usar `secure=True` em produção
```python
secure=True if os.getenv('FLASK_ENV') == 'production' else False
```

#### 3. **conexao Global não testada**
**Arquivo**: `DB_data.py` (linhas 23-24)
```python
conexao = get_conexao()
cursor = conexao.cursor()
```
**Problema**: Se conexão falhar na inicialização, Todo o app quebra
**Solução**: Fazer lazy initialization ou melhorar error handling

### 🟡 IMPORTANTES

#### 4. **Função token_required não é Decorator corretamente**
**Arquivo**: `routes.py` (linhas 17-38)
```python
def token_required(f):
    def decorated(*args, **kwargs):
        # ...sem usar functools.wraps
```
**Problema**: Metadados da função original são perdidos (erros de debug confusos)
**Solução**: Adicionar `functools.wraps`
```python
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # ...
```

#### 5. **Importação circular possível**
**Arquivo**: `routes.py` (linha 3)
```python
from main import app
```
**Arquivo**: `main.py` (linha 13)
```python
from routes import *
```
**Problema**: main importa routes, routes importa app de main
**Risco**: Pode causar importação circular
**Solução**: Mover `app = Flask(__name__)` para arquivo separado (`app.py`)

#### 6. **Token expirado não remove cookie**
**Arquivo**: `routes.py` (linhas 52-59)
```python
except jwt.ExpiredSignatureError:
    print("Token expirado...")
    pass
```
**Problema**: Cookie inválido continua no navegador
**Solução**: Remover o cookie expirado
```python
except jwt.ExpiredSignatureError:
    response = make_response(redirect(url_for('inicio')))
    response.delete_cookie('auth_token')
    return response
```

### 🔵 MELHORIAS

#### 7. **Validação de entrada no cadastro**
**Arquivo**: `routes.py` (linhas 102-104)
```python
usuário = request.form.get('email')
senha1 = request.form.get('senha1')
senha2 = request.form.get('senha2')
if senha1 and senha2:  # Verifica apenas se não são None/vazio
```
**Melhoria**: Adicionar validação de email e força de senha
```python
import re
from werkzeug.security import generate_password_hash

# Validar email
if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', usuário):
    flash('Email inválido.')
    return redirect(url_for('cadastro'))

# Validar força da senha (mínimo 8 caracteres)
if len(senha1) < 8:
    flash('Senha deve ter no mínimo 8 caracteres.')
    return redirect(url_for('cadastro'))
```

#### 8. **Usar utcnow() deprecated**
**Arquivo**: `routes.py` (linha 84)
```python
now = datetime.utcnow()
```
**Problema**: `utcnow()` está deprecated no Python 3.12+
**Solução**: Usar `datetime.now(timezone.utc)`
```python
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
```

#### 9. **Falta logging adequado**
**Problema**: Usa `print()` e perderia informações importantes
**Solução**: Implementar logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Usuário {email} realizou login")
logger.error(f"Erro ao validar token: {erro}")
```

#### 10. **Falta proteção CSRF**
**Arquivo**: Todo arquivo de formulários HTML
**Problema**: Sem CSRF token nos formulários
**Solução**: Usar Flask-WTF
```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
```

---

## 📊 Prioridade das Correções

| Prioridade | Item | Severidade |
|-----------|------|-----------|
| 1 | Token expirado não remove cookie (item 6) | 🔴 Crítica |
| 2 | secure=False do cookie (item 2) | 🔴 Crítica |
| 3 | Error handling genérico (item 1) | 🟡 Importante |
| 4 | Importação circular (item 5) | 🟡 Importante |
| 5 | Decorator sem functools.wraps (item 4) | 🟡 Importante |
| 6 | Validação de email/senha (item 7) | 🔵 Melhoria |
| 7 | Usar timezone.utc (item 8) | 🔵 Melhoria |
| 8 | Implementar logging (item 9) | 🔵 Melhoria |
| 9 | Proteção CSRF (item 10) | 🟡 Importante |

---

## 🔧 Status dos Arquivos Modificados

- ✅ `login/cadastrar.py` - Correções aplicadas ✔
- ✅ `login/validação.py` - Correções aplicadas ✔
- ✅ `routes.py` - Correções parciais aplicadas (JWT timestamps) ✔
- ⚠️ `routes.py` - Requer mais correções de segurança

