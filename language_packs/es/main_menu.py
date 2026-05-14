# Pestaña de Menu Principal - cadenas en espanol

# General
STATUS_GAME_NOT_DETECTED = "JUEGO NO DETECTADO"

# Tooltips de botones de la pestaña principal
TIP_BTN_GAME_BROWSE = "Abrir la carpeta de mods del perfil actual y el destino del symlink."
TIP_BTN_OPEN_CUSTOM_SETTINGS = "Opciones de inicio y ajustes personalizados."
TIP_BTN_FIRST_TIME_SETUP = "Crear raiz, instalar UnRAR, configurar clave API."
TIP_BTN_SELECT_ALL = "[SELECCIONAR/DESELECCIONAR TODO]"
TIP_BTN_DELETE_SELECTED = (
    "Eliminar mod(s) seleccionados de la carpeta de origen de instalacion.\n"
    "> Esto no se puede deshacer (hay un aviso de confirmacion antes de eliminar)"
)
TIP_BTN_INSTALL_SELECTED = (
    "Instalar manualmente mod(s) seleccionados en el perfil actual.\n"
    "> Los metadatos no se guardan durante instalaciones manuales.\n"
    "   > Si el mod que instalas es nuevo, deberas abrir la pestaña de gestion despues de instalar,.. \n"
    "   > ...hacer clic derecho en el archivo y establecer manualmente el ID/URL de Nexus para que CZT recupere y guarde los metadatos del mod.\n"
    "> Puedes instalar de forma segura mods existentes para actualizarlos.\n"
)
TIP_PATH_MODE_MANUAL = (
    "ACTIVADO = El usuario puede establecer manualmente rutas para el EXE y donde se enlazaran los mods al iniciar.\n"
    "[IMPORTANTE] Lee el registro que aparece despues de seleccionar esta opcion para mas informacion."
)
TIP_PATH_MODE_STEAM = (
    "ACTIVADO (PREDETERMINADO) = CZT utilizara tu STEAM library.vdf para establecer automaticamente todas las rutas necesarias.\n"
    "Haz clic en 'Detect Steam' para usar auto-ruteo."
)
TIP_BTN_MANAGE_MODS = "Unete al Discord de CZT Mod Manager para actualizaciones y soporte."
TIP_BTN_CLEAN_MOD_LIST = (
    "4 Opciones:\n"
    "- Eliminar symlinks existentes del perfil.\n"
    "- Eliminar registros del monitor de fallos.\n"
    "- Eliminar historial de descargas.\n"
    "- Quitar entradas obsoletas del archivo de lista de mods."
)
TIP_BTN_DONATIONS = "¡Gracias por usar CZT!\nHaz clic aqui para abrir la pagina de donaciones (Paypal)"
TIP_BTN_UPDATE_CZT = (
    "Haz clic para abrir las instrucciones de CZT Mod Manager.\n\n"
    "[ATAJOS]\n"
    "- Presiona SHIFT + H para mostrar los atajos disponibles.\n"
    "- Presiona F2 para abrir el menu de orden de carga."
)

# Etiquetas de la pestaña principal
LBL_PATH_MODE_MANUAL = "Manual"
LBL_PATH_MODE_STEAM = "Steam"
TAB_TITLE_MAIN_MENU = "Menu Principal"

# Etiquetas de boton/seccion de la pestaña principal
LBL_PATH_MODES = "Modos de Ruta"
LBL_BTN_DETECT_STEAM = "Detectar Steam"
LBL_BTN_SAVE_CONFIG = "Guardar Config"
LBL_BTN_SET_INSTALL_DIRECTORY = "Establecer Directorio de Instalacion"
LBL_BTN_SET_EXE_PATH = "Establecer Ruta EXE"
LBL_BTN_LAUNCH_GAME = "Iniciar Juego"
LBL_BTN_BROWSE = "Explorar"
LBL_BTN_SETTINGS = "Ajustes"
LBL_BTN_SETUP = "Configurar"
LBL_BTN_GUIDE = "Guia"
LBL_BTN_DISCORD = "Discord"
LBL_BTN_CLEAN = "Limpiar"
LBL_BTN_DONATIONS = "Donaciones"
LBL_BTN_PATCH_NOTES = "Notas de versión"
TIP_BTN_PATCH_NOTES = "Ver las notas de la versión de CZT Mod Manager y buscar actualizaciones."

# Etiquetas de estadisticas de almacenamiento de la pestaña principal
LBL_STORAGE_OVERVIEW = "[Resumen CZT]"
LBL_STATS_DISK_USAGE_TOTAL = "CZT - Almacenamiento usado:"
LBL_STATS_MODS_ENABLED = "Mods Activados: {count}"
LBL_STATS_MODS_DISABLED = "Mods Desactivados: {count}"
LBL_STATS_MODS_ENABLED_VALUE_FMT = "tamano en disco: {size}"
LBL_STATS_MODS_DISABLED_VALUE_FMT = "tamano en disco: {size}"
LBL_STATS_UPDATES_AVAILABLE = "Actualizaciones Disponibles: {count}"
LBL_STATS_APP_CPU_USAGE = "CZT - Uso de CPU:"
LBL_STATS_APP_RAM_USAGE = "CZT - Uso de RAM:"
LBL_STATS_NETWORK_SPEED = "Velocidad de red:"
LBL_STATS_DISK_RW_SPEED = "Velocidad de Lectura | Escritura:"
LBL_STATS_DISK_TRANSFER_RATE = "Tasa de Transferencia:"
LBL_STATS_UPDATES_VALUE_FMT = "escaneado: {date}"
LBL_STATS_LAST_CHECKED_NEVER = "nunca"
LBL_STATS_NETWORK_VALUE_FMT = "↑ {sent} | ↓ {recv}"
LBL_STATS_DISK_RW_VALUE_FMT = "L {read} | E {write}"
LBL_STATS_DISK_TRANSFER_VALUE_FMT = "{total}"
LBL_STATS_UNAVAILABLE = "No Disponible"

TIP_STORAGE_OVERVIEW_CUSTOMIZE = "Haz clic para personalizar los widgets de Resumen CZT: reordena filas o cambia lo que se muestra."
TIP_OVERVIEW_ITEM_UPDATES_AVAILABLE = "Muestra cuantos mods tienen actualizaciones disponibles.\n ↳ escaneado: (fecha) es la fecha del escaneo completo/automatico mas reciente."
TIP_OVERVIEW_ITEM_MODS_ENABLED = "Mods activados (cantidad) para el perfil actual:\n ↳ tamano total de la carpeta de mods 'activados' del perfil actual."
TIP_OVERVIEW_ITEM_MODS_DISABLED = "Mods desactivados (cantidad) para el perfil actual:\n ↳ tamano total de la carpeta de mods 'desactivados' del perfil actual."
TIP_OVERVIEW_ITEM_DISK_USAGE_TOTAL = "Almacenamiento usado por CZT (tamano de la carpeta raiz del usuario)\n / capacidad total de la unidad que aloja tu carpeta raiz de CZT."
TIP_OVERVIEW_ITEM_APP_CPU_USAGE = "Uso de CPU de CZT | uso de CPU del sistema | velocidad actual del reloj de CPU."
TIP_OVERVIEW_ITEM_APP_RAM_USAGE = "Uso de RAM de CZT | RAM total del sistema."
TIP_OVERVIEW_ITEM_NETWORK_SPEED = "Velocidad en vivo de subida y bajada de red del sistema."
TIP_OVERVIEW_ITEM_DISK_RW_SPEED = "Velocidad en vivo de lectura y escritura para la unidad seleccionada (unidad)."
TIP_OVERVIEW_ITEM_DISK_TRANSFER_RATE = "Tasa en vivo combinada de transferencia de lectura + escritura para la unidad seleccionada (unidad)."

DLG_TITLE_STORAGE_WIDGETS = "Personalizar Resumen CZT"
DLG_STORAGE_WIDGETS_DESC = "Arrastra elementos para reordenar. Las filas marcadas se muestran en Resumen CZT."
LBL_STORAGE_WIDGETS_DRIVE_LABEL = "Selecciona la unidad para el resumen de L/E y Tasa de Transferencia:"
LBL_STORAGE_WIDGETS_DRIVE_ALL = "Todas"
BTN_STORAGE_WIDGETS_RESTORE_DEFAULT = "Restaurar por Defecto"
BTN_STORAGE_WIDGETS_CANCEL = "Cancelar"
BTN_STORAGE_WIDGETS_APPLY = "Aplicar"
MSG_STORAGE_WIDGETS_NONE_SELECTED_TITLE = "No hay Widgets Seleccionados"
MSG_STORAGE_WIDGETS_NONE_SELECTED_BODY = "Selecciona al menos un widget para mostrar."
MSG_STORAGE_WIDGETS_TOO_MANY_TITLE = "Demasiados Widgets"
MSG_STORAGE_WIDGETS_TOO_MANY_BODY = "Este panel admite hasta {max_visible} widgets visibles al mismo tiempo."

# Titulos de ventanas emergentes de configuracion de la pestaña principal
DLG_TITLE_CUSTOM_SETTINGS = "Ajustes Personalizados"
DLG_TITLE_FIRST_TIME_SETUP = "Configuracion Inicial"

# Mensajes de registro de la pestaña principal
LOG_ROOT_MISSING = (
    "\n❌ [ERROR] ¡Carpeta raiz no configurada/no existe! \n"
    "⚠️ [WARNING] ¡Cualquier ajuste que intentes aplicar no se guardara hasta que la raiz sea creada!\n"
    "❓ [HINT] Haz clic en el boton 'SETUP' de arriba...\n"
    "  1: Haz clic en 'CREATE ROOT' y selecciona tu unidad preferida para crear las carpetas requeridas.\n"
    "  2: Haz clic en 'INSTALL UNRAR' despues de crear las carpetas raiz.\n"
    "    - Haz clic de nuevo en instalar unrar despues de instalar para configurar su ruta.\n"
    "  3: Reinicia CZT despues de instalar UnRAR.exe\n"
)

# Mensajes de utilidad de limpieza
MSG_ROOT_NOT_SET_CLEAN = "La carpeta raiz no esta configurada. No se puede limpiar la lista de mods."
MSG_NO_VALID_INSTALL_DIR = (
    "¡No hay un directorio de instalacion valido configurado!\n \n- Modo de Ruta [STEAM]:\n   > Haz clic en 'Detect Steam'\n "
    "\n- Modo de Ruta [Manual]:\n   > Haz clic en 'SET INSTALL' y 'SET EXE' para configurar."
)
LOG_CLEAN_HISTORY_CLEARED = "[CLEAN] Historial limpiado en {history_path}."
LOG_CLEAN_HISTORY_CLEAR_FAILED = "[CLEAN] Error al limpiar {history_name} en {history_path}: {error}"
LOG_CLEAN_CRASH_LOG_CLEARED = "[CLEAN] Registros del monitor de fallos limpiados: {log_path}"
LOG_CLEAN_CRASH_LOG_CLEAR_FAILED = "[CLEAN] Error al limpiar registro de fallo {log_name} en {log_path}: {error}"
LOG_CLEAN_MOD_LIST_UPDATE_FAILED = "[CLEAN] Error al actualizar lista de mods: {error}"
LOG_CLEAN_STALE_ENTRIES_REMOVED = "[CLEAN] Se eliminaron {removed} entrada(s) obsoleta(s) de mod_list.json para el perfil '{profile_name}'."
LOG_CLEAN_NO_OPTIONS_SELECTED = "[CLEAN] No se seleccionaron opciones."
LOG_PER_FILE_SYMLINK_DISABLED = "[PER-FILE] Symlink desactivado: {path}"
LOG_PER_FILE_SYMLINK_REMOVE_FAILED = "[PER-FILE] No se pudo eliminar symlink {path}: {error}"
LOG_PER_FOLDER_LINK_DISABLED = "[PER-FOLDER] Symlink/junction desactivado: {path}"
LOG_PER_FOLDER_LINK_REMOVE_FAILED = "[PER-FOLDER] No se pudo eliminar symlink/junction {path}: {error}"
LOG_LINK_MODS_JUNCTION_DISABLED = "[LINK] Junction de Mods desactivado: {path}"
LOG_LINK_MODS_SYMLINK_DISABLED = "[LINK] Symlink de Mods desactivado: {path}"
LOG_LINK_MODS_SYMLINK_REMOVE_FAILED = "[LINK] No se pudo eliminar symlink de Mods: {error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED = "[CLEAN] Se eliminaron symlinks existentes para el perfil '{profile_name}'."
LOG_CLEAN_EXE_TYPE_LINKS_REMOVED = "[{mod_type}] Se desenlazaron {count} mod(s)."
LOG_CLEAN_TYPE_SYMLINKS_REMOVED = "[{mod_type}] Se desenlazaron {count} mod(s)."
LOG_CLEAN_PER_FILE_REMOVE_FAILED_SUMMARY = "[CLEAN] No se pudieron eliminar {count} symlink(s) de mods."
LOG_CLEAN_PER_FOLDER_LINKS_REMOVED = "[PER-FOLDER] Se desenlazaron {count} mod(s)."
LOG_CLEAN_PER_FOLDER_REMOVE_FAILED_SUMMARY = "[CLEAN] No se pudieron eliminar {count} enlace(s) de carpetas de mods."
LOG_CLEAN_ERRORS_OMITTED = "[CLEAN] ...y {count} error(es) mas."
LOG_CLEAN_CONTENT_LINKS_REMOVE_FAILED = "[CLEAN] No se pudieron eliminar enlaces de mods de contenido: {error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED_SUMMARY = "[CLEAN] Se eliminaron {count} enlace(s) existentes para el perfil '{profile_name}'."

# Ventana emergente de opciones de limpieza
DLG_TITLE_CLEAN_OPTIONS = "Opciones de Limpieza"
CLEAN_OPTIONS_PROMPT = "Selecciona una o varias opciones:"
CLEAN_OPTION_STALE_ENTRIES = "Eliminar entradas obsoletas de mods_list.json."
CLEAN_OPTION_BROWSER_HISTORY = "Eliminar historial local de descargas del navegador CZT."
CLEAN_OPTION_CRASH_LOGS = "Eliminar registros del monitor de fallos."
CLEAN_OPTION_SYMLINKS = "Eliminar symlinks existentes del perfil actual."
CLEAN_OPTIONS_APPLY = "Aplicar"
CLEAN_OPTIONS_CANCEL = "Cancelar"

# Ventana emergente de configuracion inicial
LBL_FTS_CREATE_ROOT = "Crear Raiz"
LBL_FTS_INSTALL_UNRAR = "Instalar UnRAR"
LBL_FTS_NEXUS_API_KEY = "Clave API Nexus"
LBL_FTS_SAVE_KEY = "Guardar Clave"
LBL_FTS_SET_PATH = "Establecer Ruta"
LBL_FTS_OPEN_ROOT = "Abrir Raiz"

TIP_CREATE_ROOT = (
    "Haz clic en 'Create Root' y luego selecciona tu unidad preferida.\n"
    "CZT creara automaticamente las carpetas raiz y configurara la ruta de origen."
)
TIP_INSTALL_UNRAR = (
    "Descarga e instala UnRAR.exe para habilitar la extraccion de mods.\n"
    "Instala en > Unidad_Seleccionada_Para_Raiz/CZT Mod Manager/czt_tools/UnRAR.exe \n"
    "Nota: Puedes volver a hacer clic aqui despues de instalar unrar para detectar su ruta automaticamente."
)
TIP_BROWSE_UNRAR = "Selecciona la ruta de WinRAR.exe o UnRAR.exe si ya esta instalado."
TIP_NEXUS_API = (
    "Obtiene tu clave API de Nexus Mods\n"
    "Se abrira el sitio web de nexus\n"
    "Desplazate al final de la pagina abierta para ver tu clave"
)
MSG_API_KEY_SAVED_TITLE = "Clave API Guardada"
MSG_API_KEY_SAVED_TEXT = "Clave API de Nexus guardada en la configuracion."

# Ventana emergente de ajustes personalizados

SETTINGS_RESET_BUTTON_TEXT = "Restablecer"
SETTINGS_FONT_BUTTON_VALUE_TEXT = "{label}: {value}"

# Sobrescrituras de texto UI - mapea objectName del widget a texto mostrado
SETTINGS_UI_TEXT = {
    # Encabezados de grupo
    "General_Settings": "Ajustes Generales",
    "groupBox": "Ajustes Avanzados",
    "startupGroup_2": "Opciones de Color",
    "startupGroup_3": "Opciones de Fuente",
    # Etiquetas de botones de color
    "groupBoxBorderColorBtn": "Color del borde de log box",
    "logBoxBackgroundColorBtn": "Color de fondo de log box",
    "storageOverviewBorderColorBtn": "Borde de Resumen CZT",
    "lineSeparatorColorBtn": "Color del separador de linea",
    "selectedModBorderColorBtn": "Color del borde de mod seleccionado",
    "entryBorderColorBtn": "Color del borde de entrada",
    "entrySelectedBorderColorBtn": "Borde de entrada seleccionada",
    "entryBorderHoverColorBtn": "Hover del borde de entrada",
    "entryBackgroundColorBtn": "Color de fondo de entrada",
    "descriptionBackgroundColorBtn": "Fondo de descripcion",
    "descriptionBorderColorBtn": "Borde de descripcion",
    "installListBorderColorBtn": "Borde de lista de instalacion",
    "scrollbarHandleBgBtn": "BG del handle de scrollbar",
    "scrollbarHandleHoverBgBtn": "BG hover del handle de scrollbar",
    "scrollbarBorderBtn": "Borde del handle de scrollbar",
    "tabBgColorBtn": "Color de fondo de pestaña",
    "tabHoverBgBtn": "Fondo hover de pestaña",
    "tabSelectedBgBtn": "Fondo de pestaña seleccionada",
    "tabTextColorBtn": "Color de texto de pestaña",
    "tabHoverTextBtn": "Color de texto hover de pestaña",
    "tabSelectedTextColorBtn": "Color de texto de pestaña seleccionada",
    "customTabBorderColorBtn": "Color del borde de ventana",
    "modListBorderColorBtn": "Color del borde de lista de mods",
    "progressBarColorBtn": "Color de barra de progreso",
    "customColorLogBoxTextBtn": "Color de texto de log box",
    "dropdownDisplayColorBtn": "Color visible del dropdown",
    "dropdownHoverColorBtn": "Color hover del dropdown",
    "dropdownBorderColorBtn": "Color del borde del dropdown",
    "dropdownBorderHoverColorBtn": "Hover del borde del dropdown",
    "mainMenuVerticalBtnDisplayColorBtn": "Color de boton vertical del menu principal",
    "mainMenuVerticalBtnHoverColorBtn": "Hover de boton vertical del menu principal",
    "mainMenuVerticalBtnBorderColorBtn": "Borde de boton vertical del menu principal",
    "mainMenuVerticalBtnBorderHoverColorBtn": "Hover del borde de boton vertical del menu principal",
    "mainMenuHorizontalBtnDisplayColorBtn": "Color de boton de fila del menu principal",
    "mainMenuHorizontalBtnHoverColorBtn": "Hover de boton de fila del menu principal",
    "mainMenuHorizontalBtnBorderColorBtn": "Borde de boton de fila del menu principal",
    "mainMenuHorizontalBtnBorderHoverColorBtn": "Hover del borde de boton de fila del menu principal",
    "manageTopBtnDisplayColorBtn": "Color de boton superior de Manage",
    "manageTopBtnHoverColorBtn": "Hover de boton superior de Manage",
    "manageTopBtnBorderColorBtn": "Borde de boton superior de Manage",
    "manageTopBtnBorderHoverColorBtn": "Hover del borde de boton superior de Manage",
    "deleteBtnDisplayColorBtn": "Color de boton Delete",
    "deleteBtnHoverColorBtn": "Hover de boton Delete",
    "deleteBtnBorderColorBtn": "Borde de boton Delete",
    "deleteBtnBorderHoverColorBtn": "Hover del borde de boton Delete",
    "deleteBtnTextColorBtn": "Color de texto de boton Delete",
    "deleteBtnTextHoverColorBtn": "Hover de texto de boton Delete",
    "saveBtnDisplayColorBtn": "Color de boton Save",
    "saveBtnHoverColorBtn": "Hover de boton Save",
    "saveBtnBorderColorBtn": "Borde de boton Save",
    "saveBtnBorderHoverColorBtn": "Hover del borde de boton Save",
    "saveBtnTextColorBtn": "Color de texto de boton Save",
    "saveBtnTextHoverColorBtn": "Hover de texto de boton Save",
    "actionBtnDisplayColorBtn": "Color de boton de accion",
    "actionBtnHoverColorBtn": "Hover de boton de accion",
    "actionBtnBorderColorBtn": "Borde de boton de accion",
    "actionBtnBorderHoverColorBtn": "Hover del borde de boton de accion",
    "actionBtnTextColorBtn": "Color de texto de boton de accion",
    "actionBtnTextHoverColorBtn": "Hover de texto de boton de accion",
    "okBtnDisplayColorBtn": "Color de boton OK",
    "okBtnHoverColorBtn": "Hover de boton OK",
    "okBtnBorderColorBtn": "Borde de boton OK",
    "okBtnBorderHoverColorBtn": "Hover del borde de boton OK",
    "okBtnTextColorBtn": "Color de texto de boton OK",
    "okBtnTextHoverColorBtn": "Hover de texto de boton OK",
    "cancelBtnDisplayColorBtn": "Color de boton Cancel",
    "cancelBtnHoverColorBtn": "Hover de boton Cancel",
    "cancelBtnBorderColorBtn": "Borde de boton Cancel",
    "cancelBtnBorderHoverColorBtn": "Hover del borde de boton Cancel",
    "cancelBtnTextColorBtn": "Color de texto de boton Cancel",
    "cancelBtnTextHoverColorBtn": "Hover de texto de boton Cancel",
    "launchGameBtnDisplayColorBtn": "Color de boton Launch Game",
    "launchGameBtnHoverColorBtn": "Hover de boton Launch Game",
    "launchGameBtnBorderColorBtn": "Borde de boton Launch Game",
    "launchGameBtnBorderHoverColorBtn": "Hover del borde de boton Launch Game",
    "launchGameBtnTextColorBtn": "Color de texto de boton Launch Game",
    "launchGameBtnTextHoverColorBtn": "Hover de texto de boton Launch Game",
    "miscBtnTextColorBtn": "Color de texto de boton misc",
    "miscBtnTextHoverColorBtn": "Color de texto hover de boton misc",
    "miscBtnColorDisplayBtn": "Color visible de boton misc",
    "miscBtnColorHoverBtn": "Color hover de boton misc",
    "miscBtnColorBorderBtn": "Color del borde de boton misc",
    "miscBtnBorderHoverColorBtn": "Hover del borde de boton misc",
    # Etiquetas de botones de fuente
    "customFontHeaderIBtn": "Fuente de pestaña",
    "customFontHeaderMBtn": "Fuente de etiqueta",
    "customFontLogBoxBtn": "Fuente de log box",
    "customFontLabelsBtn": "Fuente de lista de mods",
    "customFontTooltipBtn": "Fuente de tooltip",
    "customFontCbBtn": "Fuente de checkbox",
    "customFontButtonBtn": "Fuente de botones",
    "customFontMainMenuVerticalButtonsBtn": "Fuente de botones izquierdos del menu principal",
    "customFontMainMenuTopButtonsBtn": "Fuente de botones superiores del menu principal",
    "customFontManageTabButtonsBtn": "Fuente de botones de la pestaña Manage",
    # Etiquetas / checkboxes generales
    "generalUseDownloadsAsSourceCheckBox": "Usar carpeta de descargas como origen.",
    "generalUseModsSourceAsSourceCheckBox": "Usar carpeta mod_staging como origen.",
    "generalUseBuiltInNexusBrowserCheckBox": "Abrir enlaces de mods usando la ventana de navegador personalizada de CZT.",
    "generalRegisterNxmHandlerCheckBox": "Configurar como gestor del boton 'Mod Manager Download'.",
    "generalUpdateOnlyEnabledModsCheckBox": "Solo revisar actualizaciones en mods activados durante escaneos.",
    "generalDownloadModsAfterScanCheckBox": "Descargar automaticamente mods marcados como 'actualizacion disponible'.",
    "generalDeleteAfterInstalledCheckBox": "Eliminar automaticamente archivos del origen despues de instalar mods.",
    "generalProtectEnabledModsFromDeletionCheckBox": "Proteger mods activados contra eliminacion.",
    "manageHomeCheckBox": "Configurar 'Manage' como pestaña de inicio.",
    "installHomeCheckBox": "Configurar 'Main Menu' como pestaña de inicio.",
    "enableCztBetaAlertsCheckBox": "Habilitar alertas para versiones beta de CZT.",
    "scanUpdatesOnStartupCheckBox": "Escanear mods en busca de actualizaciones al iniciar.",
    "updateScanCacheHoursLabel": "Frecuencia de escaneo al inicio (hrs):",
    "musicLabel": "Pista:",
    "menuMusicVolumeLabel": "Volumen:",
    "menuMusicCheckBox": "Habilitar musica del menu.",
    "pauseMenuMusicAfterLaunchCheckBox": "Pausar musica del menu despues de iniciar un juego.",
    "buttonHoverCheckBox": "Habilitar sonido de 'hover' en botones.",
    "buttonClickCheckBox": "Habilitar sonido de 'clic' en botones.",
    "languageLabel": "Idioma:",
    # Etiquetas / checkboxes avanzados
    "downloadParallelWorkersLabel": "Maximo de descargas simultaneas:",
    "backgroundThreadsLabel": "Maximo de hilos en segundo plano:",
    "installLiveLogThresholdLabel": "Umbral de registro de progreso en vivo (MB):",
    "installCacheSessionCheckBox": "Cachear seleccion de archivos (solo por sesion).",
    "installCachePersistentCheckBox": "Cachear seleccion de archivos (persistente).",
    "installCacheAutoClearCheckBox": "Limpiar automaticamente archivo de cache local persistente.",
    "installCacheMaxSizeLabel": "Umbral de autolimpieza (KB):",
    "similarityPrimaryTokensLabel": "Superposicion minima de tokens primaria:",
    "similarityPrimaryRatioLabel": "Proporcion de coincidencia primaria:",
    "generalEnableSecondaryInstallSafetyCheckBox": "Habilitar seguridad secundaria de instalacion.",
    "similaritySecondaryTokensLabel": "Superposicion minima de tokens secundaria:",
    "similaritySecondaryRatioLabel": "Proporcion de coincidencia secundaria:",
    "saveButton": "Guardar",
}

SETTINGS_HELP_TEXT = (
    "Los ajustes de abajo controlan que tan estricto es CZT al buscar posibles archivos de reemplazo durante la instalacion. "
    "Los creadores de mods a menudo renombran archivos ligeramente entre versiones, asi que CZT compara los archivos entrantes con los archivos "
    "que ya tienes y te avisa cuando encuentra una coincidencia probable.\n"
    "Las coincidencias exactas de nombre de archivo se reemplazan automaticamente. Los ajustes de abajo solo se usan para coincidencias aproximadas donde "
    "los nombres son diferentes pero aun parecen relacionados.\n\n"
    "La superposicion de tokens es cuantas partes de un nombre de archivo deben coincidir antes de tratarlo como candidato.\n"
    "La proporcion controla la estricta: valores mas bajos muestran mas candidatos (mas amplio pero menos preciso), mientras que valores mas altos "
    "muestran menos (mas preciso, pero puede perder actualizaciones validas si es demasiado alto).\n\n"
    "La seguridad secundaria es opcional y actua como una verificacion de respaldo mas amplia para capturar casos limite que la verificacion primaria podria pasar por alto."
)

TIP_REGISTER_NXM_HANDLER = (
    "Cuando esta habilitado, al hacer clic en el boton 'Mod Manager Download' en una pagina de mod, el archivo\n"
    "se envia directamente a CZT para descarga e instalacion. Todos los metadatos del mod se guardaran en el momento de la instalacion.\n"
    "- Funciona para todos los tipos de cuenta de Nexus (gratis y premium).\n"
    "NO DESACTIVAR A MENOS QUE TENGAS PROBLEMAS CON CZT SOBREESCRIBIENDO OTROS GESTORES EN EL MOMENTO DE LA DESCARGA."
)

TIP_OPEN_IN_APP_BROWSER = (
    "Cuando esta habilitado, al hacer clic en explorar, imagenes de mods o el icono de enlace, se abrira nexus dentro del navegador integrado de CZT.\n"
    "Cuando esta deshabilitado, todos los enlaces se abren en tu navegador externo predeterminado."
)

TIP_INSTALL_LIVE_LOG_THRESHOLD = (
    "Tamano minimo de instalacion antes de que CZT muestre progreso de instalacion en vivo dentro del cuadro de registro.\n"
    "Solo una ayuda visual para archivos grandes que hacen que la app parezca que no esta haciendo nada."
)

TIP_DOWNLOAD_PARALLEL_WORKERS = (
    "Cantidad maxima de descargas que CZT puede ejecutar en paralelo.\n"
    "⚠️ Valores altos pueden acelerar descargas por lotes, pero pueden causar inestabilidad."
)

TIP_BACKGROUND_THREADS = (
    "Limite de hilos en segundo plano.\n"
    "Las operaciones de escaneo de actualizaciones/loadout/instalacion se ven afectadas por este ajuste.\n"
    "Valores mas altos permiten que mas tareas se ejecuten simultaneamente.\n"
    "⚠️ Valores altos pueden acelerar acciones, pero pueden causar inestabilidad."
)

TIP_UPDATE_SCAN_CACHE_HOURS = (
    "- Si reinicias la app seguido y quieres evitar un escaneo completo al inicio, establece un valor mas alto como 6.\n"
    "- Si quieres hacer un escaneo completo en cada inicio (o cada vez que haces clic en revisar actualizaciones de todos los mods), establece esto en 0.\n"
    "- NO AFECTA LA FRECUENCIA CON LA QUE PUEDES USAR LA REVISION INDIVIDUAL DE ACTUALIZACION EN LA VENTANA \"EDIT MOD ENTRY\"."
)

TIP_SAVE_SETTINGS = (
    "Guardar ajustes y aplicar cambios.\n"
    " Nota: Es posible que ciertos ajustes requieran un reinicio para surtir efecto por completo."
)

# Tooltips de botones de restablecer
TIP_RESET_LIVE_LOG_THRESHOLD = "Restablecer umbral de progreso en vivo al valor predeterminado."
TIP_RESET_DOWNLOAD_WORKERS = "Restablecer maximo de descargas concurrentes al valor predeterminado."
TIP_RESET_BACKGROUND_THREADS = "Restablecer maximo de hilos en segundo plano al valor predeterminado."
TIP_RESET_PRIMARY_TOKENS = "Restablecer superposicion de tokens primaria al valor predeterminado."
TIP_RESET_PRIMARY_RATIO = "Restablecer proporcion primaria al valor predeterminado."
TIP_RESET_SECONDARY_TOKENS = "Restablecer superposicion de tokens secundaria al valor predeterminado."
TIP_RESET_SECONDARY_RATIO = "Restablecer proporcion secundaria al valor predeterminado."

# Tooltips de cache de instalacion
TIP_CACHE_SESSION = (
    "Almacenar seleccion de archivos de archivo comprimido de archivos conocidos hasta que CZT se cierre.\n"
    "Usa refresh para limpiar las selecciones cacheadas de la sesion."
)
TIP_CACHE_PERSISTENT = (
    "Almacenar seleccion de archivos de archivo comprimido en archivo para que persistan despues de reiniciar.\n"
    "Usa refresh para limpiar el archivo de cache local."
)
TIP_CACHE_AUTO_CLEAR = "Cuando esta habilitado, la cache persistente se limpia automaticamente al superar el limite de abajo."
TIP_CACHE_MAX_SIZE = "Tamano maximo de archivo de cache persistente en KB antes de ejecutar autolimpieza."
TIP_CLEAR_SESSION_CACHE = "Limpiar cache de seleccion de archivos de sesion."
TIP_CLEAR_PERSISTENT_CACHE = "Limpiar cache persistente de seleccion de archivos."
TIP_RESET_CACHE_SIZE_LIMIT = "Restablecer limite de tamano de cache persistente al valor predeterminado."

# Respaldo para desplegable de musica
DEFAULT_MUSIC_TRACK = "Default"

# Desplegable de idioma
LBL_LANGUAGE = "Idioma:"
TIP_LANGUAGE_DROPDOWN = (
    "Selecciona el idioma de visualizacion para CZT Mod Manager.\n"
    "Se pueden agregar paquetes de idioma adicionales en tu carpeta raiz > CZT Mod Manager/plugins/language_packs/.\n"
    "Los cambios surten efecto despues de reiniciar la aplicacion."
)
MSG_LANGUAGE_RESTART = "Idioma cambiado. Reinicia CZT Mod Manager para que el cambio surta efecto completo."

TIP_MENU_MUSIC_DROPDOWN = (
    "Selecciona la pista de musica de fondo del menu.\n"
    "Puedes agregar pistas personalizadas colocandolas en tu carpeta raiz > CZT Mod Manager/plugins/audio/menu_music.\n"
    "Formatos compatibles: .mp3, .wav, .ogg"
)
TIP_BETA_ALERTS_RESET = "Restablecer alertas beta descartadas para que el aviso de la beta mas reciente pueda mostrarse al iniciar."
TIP_INSTALL_CACHE_MAX_RESET = "Restablecer limite de tamano de cache persistente al valor predeterminado."
MSG_FONT_BLOCKED_TITLE = "Fuente Bloqueada"
MSG_FONT_BLOCKED_TEXT = "La fuente '{font_family}' no esta permitida. Selecciona una fuente diferente."
MSG_SETTINGS_SAVED_TITLE = "Ajustes Guardados"
MSG_SETTINGS_SAVED_CHANGED = "Se cambiaron los siguientes ajustes:"
MSG_SETTINGS_SAVED_NO_CHANGES = "No se cambiaron ajustes."

# Cadenas de registro/estado de controls.py
LOG_CONFIG_NOT_SAVED_NO_ROOT = "❌ [ERROR] ¡Configuracion no guardada porque czt_root_folder no esta configurada!\n    > Ve a la pestaña USER SETTINGS y haz clic en 'CREATE ROOT'"
DEFAULT_SET_PROFILE_PATH = "No configurado, si usas ruteo manual presiona [Set Install] y [Set EXE]"
DEFAULT_STEAM_LIBRARY_PATH = "No configurado, presiona [Detect Steam]"
DEFAULT_CURRENT_PROFILE = "No configurado, selecciona un perfil valido."
DEFAULT_EXE_NOT_FOUND = "No encontrado, \n    Usuarios Steam: Presiona [Detect Steam], luego [Launch Game]\n     Usuarios Manual: Presiona [Set EXE] para resolver."
LOG_SAVE_CONFIG_SUMMARY = (
    "[SAVE CONFIG] Guardado ✓\n"
    "[RESUMEN RAPIDO CFG]\n"
    "⇾ Perfil Actual: {current_profile}\n"
    "⇾ Modo de Ruta: {profile_path_mode}\n"
    "⇾ Destino SymLink: {set_profile_path}\n"
    "⇾ EXE Destino: {exe_path}"
)
LOG_AUTO_SAVE_NO_ROOT = "❌ [ERROR] No hay czt_root_folder configurada. ¡Configuracion no guardada!"
LOG_BROWSE_NO_ROOT = "\n[ERROR] ¡No hay carpeta raiz configurada! Haz clic en 'CREATE ROOT' para empezar a usar CZT.\n"
LOG_PROFILE_MODS_FOLDER_NOT_FOUND = "[ERROR] No se encontro la carpeta de mods del perfil: {profile_mods_path}"
LOG_DEST_FOLDER_NOT_FOUND = "[ERROR] No se encontro la carpeta de destino."
LOG_OPENED_INSTALL_AND_MODS = "Ubicacion de instalacion del juego y carpeta Mods abiertas."
LOG_SELECTED_PROFILE = "[PROFILE] Perfil seleccionado: {current_profile}"
LOG_PROFILE_FOLDER_WARN = "[PROFILE][WARN] No se pudieron asegurar las carpetas del perfil para '{current_profile}': {error}"
