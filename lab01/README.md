# Laboratorio 1 · Exploración guiada de servicios Azure

**Proyecto Integrador:** Copiloto Cognitivo de Asistencia Bancaria  
**Entrega:** rama `lab-01/jorgecr1991`

Reproduce las pruebas de la sesión de nivelación (Document Intelligence y Content Safety) con **datos 100% sintéticos** del caso
y autenticación por **Microsoft Entra ID + Azure CLI**, sin API keys.

## Contenido

| Ruta | Qué es |
| --- | --- |
| `lab01_00_validacion_azure.ipynb` | A. Validación de conexión: `az --version`, `az account show`, token de Entra ID y acceso a ambos recursos |
| `lab01_01_document_intelligence_copiloto.ipynb` | B. Listado de modelos, `prebuilt-layout`, `prebuilt-invoice`, JSON indexable, aplicación y reflexión |
| `lab01_02_content_safety_blocklist_copiloto.ipynb` | C. Análisis por categoría y severidad, política de acciones, blocklist propia (13 términos), pruebas de coincidencia, aplicación y reflexión |
| `data/ficha_tarjetas_credito_banco_andino.pdf` | Documento sintético principal (2 páginas): ficha de producto y guía de atención de tarjetas “Cóndor” de un banco ficticio |
| `data/factura_sintetica_plasticos_andes.pdf` | Factura ficticia de 1 página para `prebuilt-invoice` |
| `scripts/generar_pdfs_sinteticos.py` | Regenera los dos PDF |
| `outputs/` | Resultados generados al ejecutar los notebooks (JSON indexable y Markdown de layout) |
| `.env.example` | Variables necesarias (solo endpoints y nombres) |

## Cómo ejecutarlo

1. Portal de Azure con la cuenta asignada (Cuenta profesional o educativa) y Microsoft Authenticator configurado.
2. En la terminal de VS Code:
   ```powershell
   az --version
   az login          # cuenta asignada para el laboratorio
   az account show
   ```
3. Configuración: crea `labs/lab01/.env` desde `.env.example` con los endpoints del recurso asignado. Si no existe, se usa el `.env` del curso (`Notebooks/.env`).
4. Abre los notebooks en orden (00 → 01 → 02) con el kernel **Python (Cognitive AI)** y ejecuta **Run All**.
5. Si aparece 401/403: no modificar roles ni políticas; anotarlo en el notebook 00 y avisar al instructor.

## Reglas cumplidas

- Sin API keys en código, notebooks ni `.env` (el loader valida que el `.env` no tenga variables tipo `KEY`/`SECRET`).
- Datos 100% sintéticos: banco, productos, montos, RUC, personas y direcciones ficticios.
- Blocklist con nombre único en el recurso compartido: `blocklist-copiloto-bancario-jorgecr1991`.
- Identificadores de suscripción y tenant enmascarados en las salidas.

## Checklist de validación

- [ ] Conexión con Azure validada con la identidad del participante, sin API keys.
- [ ] Pruebas de Document Intelligence con documentos sintéticos y resultados documentados.
- [ ] Pruebas de Content Safety con mensajes sintéticos y blocklist propia creada.
- [ ] Reflexión final en cada notebook.
