# Pestaña del Gestor de Mods - cadenas en espanol

# === Tooltips de botones ===
TIP_SELECT_ALL          = "Seleccionar todos los mods"
TIP_TOGGLE_ALL          = "Activar/Desactivar todos los mods"
TIP_QUICK_SAVE          = "Guardar mods activados como un loadout"
TIP_RESTORE_BACKUP      = "Restaurar desde la lista de copias"
TIP_SCAN_UPDATES        = "Comprobar actualizaciones de todos los mods"
TIP_BROWSE_NEXUS        = "Explorar Nexus Mods para este juego"
TIP_DOWNLOAD_SELECTED   = "Descargar mods seleccionados (Shift+D)"
TIP_DISABLE             = "Desactivar mods seleccionados"
TIP_RESTORE_DISABLED    = "Restaurar mods desactivados"
TIP_DELETE              = "Eliminar mods seleccionados"
TIP_CREATE_BACKUP       = "Crear copia de seguridad de mods y/o mods_list.json."
TIP_HIDE_DISABLED       = "Ocultar mods desactivados de la lista/cuadricula"
TIP_VIEW_LIST           = "Vista de lista"
TIP_VIEW_GRID           = "Vista de cuadricula"

# === Etiquetas de pestaña principal ===
TAB_TITLE_MANAGE_MODS   = "Gestionar Mods"
LBL_HIDE_DISABLED       = "Ocultar Desactivados"

# === Desplegable de Loadouts ===
BTN_LOADOUTS = "Loadouts"
TIP_LOADOUTS = (
    "1.) Empieza desactivando todos tus mods, luego activa los mods que quieres para el nuevo loadout.\n"
    "2.) Haz clic en el icono de guardar para guardar los mods activados como un archivo de loadout.\n"
    " - Los loadouts guardados se pueden cambiar desde este desplegable en cualquier momento.\n"
    " - En Gestionar Todo, cada fila de loadout tiene iconos de renombrar, copiar archivo y descargar.\n"
    " - Usa 'Importar desde archivo' para agregar loadouts desde otro archivo JSON.\n"
    " - Tambien puedes eliminar/editar informacion del loadout haciendo clic en 'Gestionar Todo'."
)
LBL_LOADOUTS_HEADER_SAVED = "Loadouts Guardados"
LBL_LOADOUTS_EMPTY = "No hay loadouts"
LBL_LOADOUTS_HEADER_MANAGE = "Gestionar"
BTN_LOADOUT_MANAGER = "Gestor de Loadouts"
LBL_LOADOUTS_HEADER_QUICK_ACTIONS = "Acciones Rapidas"
BTN_IMPORT_LOADOUT_FILE = "Importar Archivo de Loadout"
BTN_IMPORT_DOWNLOAD_LOADOUT = "Importar + Descargar Loadout"

# === Barra de busqueda ===
SEARCH_PLACEHOLDER = "Buscar mods : {profile}"

# === Ordenar / Filtrar ===
TIP_SORT_BY_MOD_NAME    = "Ordenar por nombre del mod"
TIP_SORT_BY_CREATOR     = "Ordenar por creador"
BTN_SORT_FILTER         = "Ordenar/Filtrar"

SORT_SECTION_DISPLAY_NAME   = "Nombre para mostrar"
SORT_AZ_DISPLAY_NAME        = "Nombre para mostrar A-Z"
SORT_ZA_DISPLAY_NAME        = "Nombre para mostrar Z-A"

SORT_SECTION_CREATOR    = "Creador"
SORT_AZ_CREATOR         = "Creador A-Z"
SORT_ZA_CREATOR         = "Creador Z-A"

SORT_SECTION_CATEGORY   = "Categoria"
SORT_AZ_CATEGORY        = "Categoria A-Z"
SORT_ZA_CATEGORY        = "Categoria Z-A"

SORT_SECTION_STATUS         = "Estado"
SORT_FAVORITES              = "Favoritos (arriba)"
SORT_UPDATES_AVAILABLE      = "Actualizaciones disponibles (arriba)"
SORT_MOD_HIDDEN             = "Mod Oculto (arriba)"
SORT_MOD_REMOVED            = "Mod Eliminado (arriba)"
SORT_CORRUPTED              = "Corrupto (arriba)"
SORT_ENABLED                = "Activado (arriba)"
SORT_DISABLED               = "Desactivado (arriba)"

SORT_SECTION_FILE_SIZE  = "Tamano de archivo"
SORT_SMALLEST           = "Mas pequeno primero"
SORT_LARGEST            = "Mas grande primero"

SORT_SECTION_INSTALL_DATE   = "Fecha de instalacion"
SORT_NEW_TO_OLD             = "Nuevo a antiguo (hora de instalacion)"
SORT_OLD_TO_NEW             = "Antiguo a nuevo (hora de instalacion)"

# === Dialogo de eliminar mods ===
DLG_DELETE_TITLE            = "¿Eliminar ({count}) mods?"
BTN_YES_DELETE              = "Si, Eliminar"
BTN_CANCEL                  = "Cancelar"
MSG_NO_MODS_SELECTED_DELETE = "No se seleccionaron archivos de mod para eliminar."
MSG_ENABLED_MODS_SKIPPED    = "Se omitieron mods activados porque 'Proteger mods activados contra eliminacion' esta habilitado."
MSG_MODS_DIR_NOT_FOUND      = "No se encontro el directorio de mods. Configura una carpeta raiz valida."

# === Eliminacion por mod ===
DLG_DELETE_MOD_TITLE        = "Eliminar Mod"
MSG_CONFIRM_DELETE_MOD      = "¿Eliminar este mod?\n{filename}"

# === Desactivar mods ===
MSG_NO_MODS_SELECTED_DISABLE    = "No se seleccionaron archivos de mod para desactivar."
DLG_DISABLE_TITLE               = "Desactivar Mods"
MSG_CONFIRM_DISABLE             = "¿Seguro que quieres desactivar los mods seleccionados?"
MSG_DISABLED_WITH_ERRORS        = "Se desactivaron {moved} mod(s), pero ocurrieron {errors} error(es)."
MSG_DISABLED_OK                 = "Se desactivaron {moved} archivo(s) de mod."

# === Dialogo de restaurar mods desactivados ===
MSG_NO_DISABLED_FOLDER          = "No se encontro carpeta de mods desactivados."
MSG_NO_MODS_TO_RESTORE          = "No hay mods para restaurar en la carpeta de desactivados."
DLG_RESTORE_TITLE               = "Restaurar Mods Desactivados"
LBL_RESTORE_CONFIRM             = "¿Restaurar estos mods?"
BTN_SELECT_ALL                  = "Seleccionar Todo"
BTN_DESELECT_ALL                = "Deseleccionar Todo"
BTN_RESTORE_SELECTED            = "Restaurar Seleccionados"
MSG_RESTORED_WITH_ERRORS        = "Se restauraron {restored} mod(s), pero ocurrieron {errors} error(es)."
MSG_RESTORED_OK                 = "Se restauraron {restored} archivo(s) de mod."

# === Mensajes de Toggle/Log ===
LOG_TYPE_DISABLED               = "[{mod_type}] Se desactivaron {count} mod(s)"
LOG_TYPE_ENABLED                = "[{mod_type}] Se activaron {count} mod(s)"
LOG_MOD_LIST_ITEM               = "  - {mod_name}"
LOG_DISABLE_TOTAL               = "[DISABLE] Se desactivaron {count} mod(s) correctamente."
LOG_DISABLE_FAILED_ITEM         = "[{mod_type}] Error al desactivar mod {mod_name}: {error}"
LOG_ENABLE_FAILED_ITEM          = "[{mod_type}] Error al activar mod {mod_name}: {error}"

# === Enlaces de mods ===
MSG_NO_MOD_LINKS        = "No se encontraron enlaces de mods para abrir."
MSG_CONFIRM_OPEN_LINKS  = "¿Abrir enlaces para {count} mod(s) seleccionados?"
MSG_OPEN_LINKS_INFO     = "Esto abrira {count} pestaña(s) del navegador."

# === Ventana emergente de informacion del mod ===
TIP_REFRESH_NEXUS       = "Actualizar info de Nexus y volver a descargar imagen"
TIP_DOWNLOAD_NEXUS      = "Descargar el archivo mas reciente desde Nexus"
BTN_CHECK_FOR_UPDATE    = "Buscar Actualizacion"
DLG_TITLE_EDIT_MOD_ENTRY = "Editar Entrada de Mod"
LBL_EDIT_NAME           = "Nombre:"
LBL_EDIT_CREATOR        = "Creador:"
LBL_EDIT_FILE           = "Archivo:"
LBL_EDIT_SIZE           = "Tamano:"
LBL_EDIT_VERSION        = "Version:"
LBL_EDIT_INSTALL_DATE   = "Fecha de Instalacion:"
LBL_EDIT_STATUS         = "Estado:"
LBL_EDIT_DISPLAY_NAME   = "Nombre para mostrar"
LBL_EDIT_NEXUS_ID_URL   = "ID o URL del Mod en Nexus"
BTN_SAVE                = "Guardar"
FMT_LOCAL_LATEST        = "Local: {local_version} | Ultima: {latest_version}"
LBL_STATUS_ENABLED      = "Activado"
LBL_STATUS_DISABLED     = "Desactivado"
LBL_NO_IMAGE            = "Sin imagen"
LBL_ROW_CATEGORY        = "Categoria"
LBL_ROW_SIZE            = "Tamano"
LBL_ROW_FILE            = "Archivo"
LBL_ROW_LOCAL           = "Local"
LBL_ROW_LATEST          = "Ultima"
LBL_ROW_INSTALL         = "Instalacion"
LBL_ROW_MOD_ID          = "ID Mod"
TAG_VALID_UP_TO_DATE    = "Valido y al dia"
TAG_UPDATE_REMOVED      = "Eliminado"
TAG_UPDATE_HIDDEN       = "Oculto"
TAG_UPDATE_AVAILABLE    = "Actualizacion Disponible"
TAG_REMOVED_DELETED     = "Eliminado/Borrado"
TAG_CORRUPTED           = "Corrupto"

# === Dialogo de opciones de actualizacion forzada ===
DLG_FORCE_UPDATE_TITLE      = "Opciones de Actualizacion Forzada"
LBL_FORCE_UPDATE_PROMPT     = "¿Que atributos quieres forzar a actualizar?"
CB_DISPLAY_NAME             = "Nombre para mostrar"
CB_THUMBNAIL                = "Miniatura / Imagen"
CB_INSTALL_DATE             = "Fecha de instalacion"
CB_LOCAL_VERSION            = "Version local (para mods tipo data2.pak, data3.pak, etc.)"
BTN_APPLY                   = "Aplicar"
