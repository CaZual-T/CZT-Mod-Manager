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
TIP_BROWSE_UNRAR = (
    "Establece la ruta a UnRAR.exe (o WinRAR.exe) ubicado en cualquier lugar de tu PC.\n"
    "Busca el archivo, o pega su ruta completa en la casilla y presiona Enter para guardar."
)
TIP_NEXUS_API = (
    "Obtiene tu clave API de Nexus Mods\n"
    "Se abrira el sitio web de nexus\n"
    "Desplazate al final de la pagina abierta para ver tu clave"
)
MSG_API_KEY_SAVED_TITLE = "Clave API Guardada"
MSG_API_KEY_SAVED_TEXT = "Clave API de Nexus guardada en la configuracion."
MSG_UNRAR_PATH_INVALID_TITLE = "Ruta de UnRAR invalida"
MSG_UNRAR_PATH_INVALID_TEXT = (
    "Esa ruta no apunta a un UnRAR.exe o WinRAR.exe valido.\n"
    "Busca el archivo o pega su ruta completa y presiona Enter."
)

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

# ============================================================
# Custom Profiles popup (F6)
# ============================================================
DLG_TITLE_CUSTOM_PROFILES = "Perfiles Personalizados"
LBL_CUSTOM_PROFILES_TITLE = "Perfiles de Juego Personalizados"
LBL_CUSTOM_PROFILES_SUBTITLE = (
    "Agrega tus propios juegos. Los campos en blanco heredan valores predeterminados sensatos del motor."
)
LBL_EDITING = "Editando:"
LBL_PROFILE_NAME = "Nombre del Perfil *"
LBL_ENGINE = "Motor *"
LBL_ENGINE_DESCRIPTION = "Descripcion:"
LBL_STEAM_APPID = "ID de App de Steam"
LBL_LAUNCH_EXE = "Ejecutable de Inicio"
LBL_GAME_PATH = "Ruta de Mods del Juego"
LBL_NEXUS_LINK = "Enlace de Nexus del Juego"
LBL_MOD_DIR_NAME = "Nombre de Carpeta de Mods"
LBL_ROUTING = "Enrutamiento de Carpetas"
LBL_DEFAULT_MODS_DIR = "Colocar los mods directamente en la carpeta raiz del perfil (sin subcarpeta 'Mods')"
OPT_NEW_PROFILE = "＋ Nuevo Perfil"
BTN_DELETE_PROFILE = "Eliminar"
BTN_SAVE_PROFILE = "Guardar Perfil"
BTN_CLOSE = "Cerrar"

# Custom Profiles - input placeholders
PH_PROFILE_NAME = "ej: Mi Juego Increible"
PH_STEAM_APPID = "ID de App de Steam (ej: 1144200)"
PH_LAUNCH_EXE = "Juego.exe"
PH_GAME_PATH = r"\Mi Juego\Mods"
PH_NEXUS_LINK = "https://www.nexusmods.com/<juego>/mods/"
PH_MOD_DIR_NAME = "Mods"
PH_ROUTING = "plugins=Plugins, config=Config"

# Custom Profiles - in-depth field tooltips
TIP_CP_PROFILE_SELECTOR = (
    "Elige que perfil editar.\n"
    "• '＋ Nuevo Perfil' abre un formulario en blanco para crear un juego nuevo.\n"
    "• Al seleccionar un perfil existente se cargan sus valores para editarlo o eliminarlo.\n"
    "Aqui solo aparecen TUS perfiles personalizados --> los perfiles integrados no se pueden editar\n"
    "ni eliminar desde esta ventana."
)
TIP_CP_PROFILE_NAME = (
    "El nombre visible de tu juego, mostrado en el desplegable de perfiles (obligatorio).\n"
    "Tambien se convierte en un nombre de carpeta real bajo tu raiz de CZT, asi que debe ser un\n"
    "nombre de carpeta valido de Windows.\n"
    "Permitido: letras, numeros, espacios, guiones, guiones bajos.\n"
    "No permitido: < > : \" / \\ | ? * , nombres que terminen en espacio o punto, y\n"
    "nombres reservados (CON, PRN, NUL, COM1…).\n"
    "Debe ser unico --> no puede coincidir con un perfil integrado u otro personalizado."
)
TIP_CP_ENGINE = (
    "El motor de mods que CZT usa para instalar y enlazar los mods de este juego (obligatorio).\n"
    "Elige el motor que coincida con tu juego (p. ej. Unreal Engine, Unity, Techland).\n"
    "El motor aporta valores predeterminados inteligentes (tipos de archivo permitidos, como se enlazan los mods),\n"
    "asi que rara vez necesitas tocar los campos avanzados de abajo.\n"
    "El texto gris bajo esta casilla resume el motor seleccionado."
)
TIP_CP_STEAM_APPID = (
    "El ID de App de Steam del juego (opcional, solo numeros).\n"
    "Lo encuentras en la URL de la tienda de Steam: store.steampowered.com/app/<APPID>/.\n"
    "CZT lo usa para localizar automaticamente el juego a traves de tu biblioteca de Steam.\n"
    "Dejalo en blanco para juegos que no son de Steam --> aun puedes definir rutas manualmente en la\n"
    "pestana del Menu Principal. Letras o simbolos aqui se rechazaran al guardar."
)
TIP_CP_LAUNCH_EXE = (
    "El ejecutable del juego, relativo a la carpeta del juego.\n"
    "Ejemplo: Juego.exe  o  Binaries\\Win64\\Juego.exe.\n"
    "Separa varios candidatos con comas --> CZT usa el primero que encuentre.\n"
    "Lo usa el boton 'Iniciar Juego'; dejalo en blanco si inicias el juego tu mismo."
)
TIP_CP_GAME_PATH = (
    "Un fragmento de ruta usado para ayudar a detectar la carpeta de mods del juego (Steam).\n"
    "Normalmente el final de la ruta de instalacion, p. ej. \\Mi Juego\\Mods.\n"
    "Separa varios candidatos con comas.\n"
    "Esto es una pista de deteccion, no una ruta completa --> para control manual total, define la\n"
    "ruta de instalacion del juego en la pestana del Menu Principal despues de guardar."
)
TIP_CP_NEXUS_LINK = (
    "La pagina de Nexus Mods de este juego.\n"
    "Formato: https://www.nexusmods.com/<juego>/mods/  donde <juego> es el dominio\n"
    "mostrado en la URL del sitio para ese juego.\n"
    "Habilita el navegador de Nexus integrado y los enlaces 'abrir en Nexus' para este perfil."
)
TIP_CP_MOD_DIR_NAME = (
    "El nombre de la carpeta del lado del juego donde se enlazan los mods.\n"
    "Valores comunes: Mods, Paks, source. Por defecto es 'Mods' si se deja en blanco.\n"
    "Se ignora cuando 'Colocar los mods directamente en la carpeta raiz del perfil' esta marcado.\n"
    "Si no estas seguro, deja el valor predeterminado --> el motor suele gestionarlo correctamente."
)
TIP_CP_ROUTING = (
    "Avanzado: envia carpetas especificas de nivel superior a una carpeta distinta del lado del juego\n"
    "(opcional).\n"
    "- Formato: origen=Destino, separado por comas. Ejemplo: plugins=Plugins, config=Config.\n"
    "- Significado: una carpeta 'plugins' dentro de un mod se enlaza a la carpeta 'Plugins' del juego\n"
    "en lugar de la carpeta Mods normal.\n"
    "-Dejalo en blanco a menos que tu juego separe los plugins etc. de los mods normales."
)
TIP_CP_DEFAULT_MODS_DIR = (
    "Cuando esta marcado, los mods se colocan directamente en la carpeta raiz del perfil en lugar\n"
    "de una subcarpeta 'Mods'.\n"
    "Usa esto para juegos que cargan los mods directamente desde la raiz del juego.\n"
    "Cuando esta marcado, se ignora el 'Nombre de Carpeta de Mods' de arriba.\n"
    "Dejalo sin marcar para el caso tipico (los mods viven en una carpeta Mods dedicada)."
)
TIP_CP_SAVE = (
    "Valida y guarda este perfil.\n"
    "Los perfiles nuevos aparecen de inmediato en el desplegable de perfiles; editar actualiza la\n"
    "entrada existente.\n"
    "Se guarda en custom_profiles.json en tu carpeta raiz de CZT."
)
TIP_CP_DELETE = (
    "Elimina el perfil personalizado seleccionado.\n"
    "Esto solo quita la entrada del perfil --> NO elimina ningun mod instalado\n"
    "ni archivos en el disco.\n"
    "Solo esta disponible para perfiles personalizados que creaste (no integrados)."
)
TIP_CP_CLOSE = (
    "Cierra esta ventana.\n"
    "Los cambios sin guardar en el formulario se descartan; los perfiles ya guardados se conservan."
)

# Custom Profiles - status / dialog messages
MSG_ENGINE_EXPERIMENTAL = (
    "⚠ Motor experimental: no probado con un juego real. Espera solo despliegue basico "
    "de archivos (sin enrutamiento especial ni gestion de orden de carga)."
)
MSG_NO_ROOT_FOLDER = "Primero define tu carpeta raiz de CZT (Configuracion Inicial)."
MSG_APPID_NUMERIC = "El ID de App de Steam debe ser numerico."
DLG_TITLE_DELETE_PROFILE = "Eliminar Perfil"
MSG_CONFIRM_DELETE_PROFILE = (
    "¿Eliminar el perfil personalizado '{name}'?\nEsto no elimina ningun mod instalado."
)

# Custom Profiles - validation / persistence messages
MSG_NAME_EMPTY = "El nombre del perfil no puede estar vacio."
MSG_NAME_INVALID_CHARS = 'El nombre no puede contener ninguno de: < > : " / \\ | ? *'
MSG_NAME_RESERVED = "'{name}' es un nombre reservado del sistema."
MSG_NAME_TRAILING = "El nombre no puede terminar con un espacio o punto."
MSG_NAME_BUILTIN = "'{name}' es un nombre de perfil integrado; elige otro."
MSG_NAME_EXISTS = "Ya existe un perfil personalizado llamado '{name}'."
MSG_SELECT_ENGINE = "Selecciona un motor para este perfil."
MSG_UNKNOWN_ENGINE = "Motor desconocido: '{engine}'."
MSG_SAVE_FAILED = "No se pudo escribir custom_profiles.json (verifica los permisos de la carpeta)."
MSG_PROFILE_SAVED = "Perfil '{name}' guardado."
MSG_NOT_CUSTOM = "'{name}' no es un perfil personalizado."
MSG_DELETE_UPDATE_FAILED = "No se pudo actualizar custom_profiles.json."
MSG_PROFILE_DELETED = "Perfil '{name}' eliminado."

FORZATECH_DESC = (
    "Motor de superposicion de archivos sueltos para Forza Horizon. Los mods son carpetas (no paks) "
    "con un arbol 'media' que sobrescribe el contenido original, un arbol aditivo 'mediapc', "
    "y/o archivos raiz como un proxy version.dll. CZT fusiona todos los mods habilitados "
    "en una sola superposicion segun el orden de carga (el de arriba gana los conflictos), luego la mapea al "
    "juego como una union por cada carpeta de nivel superior mas un enlace simbolico por cada archivo raiz. "
    "Donde ya existe una carpeta original real, superpone por archivo y respalda "
    "lo que oculta como '.czt_orig'."
)

TECHLAND_DESC = (
    "Motor de .pak basado en ranuras para el C-Engine de Techland (Dying Light 1/2, The "
    "Beast). El orden de carga proviene de los nombres numerados data##.pak, con ranuras bajas "
    "reservadas para el juego y un rango superior abierto a los mods. CZT enlaza "
    "el .pak de cada mod en la carpeta de recursos plana del juego y lo renombra a una "
    "ranura libre. Los plugins nativos .dll/.asi se enlazan junto al exe del juego. Sin "
    "carpeta Content ni audio separado - el audio va dentro de los paks."
)

UNREAL_DESC = (
    "Motor de paks para Unreal Engine 4/5. Maneja .pak heredado mas contenedores IoStore "
    ".utoc/.ucas (y archivos .sig para juegos con paks firmados). CZT enlaza "
    "los paks en la carpeta de mods del juego (LogicMods, ~mods o Mods) y los renombra "
    "por numero de pakchunk para definir el orden de carga. Admite modloaders .dll/.asi "
    "como UE4SS enlazados al exe, mas audio opcional Wwise (.bnk/.wem) y FMOD "
    "(.bank)."
)

UNITY_DESC = (
    "Motor impulsado por modloaders para Unity (BepInEx, MelonLoader, UnityModManager) "
    "- los loaders siguen gestionando el orden de carga, no el motor. Los mods suelen ser plugins .dll o "
    "paquetes de assets .bundle/.unity3d. CZT enlaza los mods .dll en la carpeta "
    "de mods del loader y enruta carpetas conocidas de nivel superior (p. ej. 'plugins') a sus "
    "equivalentes en la raiz del juego. Audio FMOD/Wwise opcional; sin concepto de pak ni "
    "carpeta Content."
)



