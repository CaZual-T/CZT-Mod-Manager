# Utilities Global - cadenas en espanol

# ===== basic_global_utilities.py =====
LOG_WARN_NO_ROOT_SAVE = "⚠️ [WARNING] No se puede guardar la configuracion porque czt_root_folder no existe."
LOG_UNRAR_NOT_FOUND = "[UNRAR] No se encontro una herramienta UnRAR funcional. Configura 'unrar_path' en ajustes o instala WinRAR (UnRAR.exe)."
DLG_TITLE_SELECT_DRIVE = "Seleccionar Unidad"
LBL_SELECT_DRIVE = "Elige una unidad para las carpetas de Mod Manager:"
BTN_OK = "Aceptar"
BTN_CANCEL = "Cancelar"

# ===== CheckForCZTUpdates.py =====
WELCOME_MESSAGE = (
    "🔄️ Instalacion automatica de mods:\n"
    "- Descarga mods desde el sitio de nexus. (usa el boton 'Mod Manager Download')\n"
    "- Esto activara CZT y la app gestionara automaticamente la instalacion + guardado de informacion del mod.\n"
    "- Si el boton 'Mod Manger Download' no existe, descarga la extension CZT desde github.\n"
    "- La extension CZT permite que el boton de descarga manual funcione como el boton 'Mod Manager Download'.\n\n"
    "🛠️ Instalacion manual de mods:\n"
    "- Arrastra y suelta archivos de mod en este cuadro de registro para prepararlos para instalacion.\n"
    "- Selecciona mods de la lista y luego haz clic en ➡️ (arriba a la derecha) para continuar.\n\n"
    "💡 [HINT]\n"
    "- La mayoria de elementos de UI tienen tooltips; pasa el cursor sobre botones y otros elementos de UI para verlos. \n"
    "- Presiona SHIFT + H para mostrar los atajos disponibles.\n"
    "- Presiona F2 para abrir el menu de orden de carga.\n"
)
DLG_TITLE_BETA_AVAILABLE = "Beta Disponible"
DLG_TITLE_UPDATE_AVAILABLE = "Actualizacion Disponible"
LBL_BETA_AVAILABLE = "¡Hay una nueva beta de CZT disponible!"
LBL_UPDATE_AVAILABLE = "¡Hay una nueva version de CZT Mod Manager disponible!"
LBL_VERSION_INFO = "Actual: {local_version}\nUltima: {latest_version}"
BTN_DOWNLOAD_INSTALL = "Descargar e Instalar ({tag})"
BTN_DISMISS = "Descartar"
BTN_IGNORE = "Ignorar"
BTN_CLOSE = "Cerrar"
BTN_CHECK_FOR_UPDATES = "Buscar actualizaciones"
MSG_HOTKEY_CONTROLS = (
    "\n\n"
    "[CONTROLES DE ATAJOS]\n"
    "    > F2           : Abrir menu de orden de carga.\n"
    "    > F3           : Abrir menu de plugins.\n"
    "    > F5           : Recentrar la ventana principal en la pantalla.\n"
    "    > F9           : Detectar mods faltantes de un loadout guardado.\n"
    "    > CTRL+O       : Abrir carpeta raiz de CZT.\n"
    "    > Shift+H      : Mostrar opciones de atajos.\n"
    "    > Shift+C      : Mostrar configuracion actual.\n"
    "    > Shift+R      : Mostrar rutas de archivos de recursos.\n"
    "    > Ctrl+Shift+L : Iniciar juego.\n"
    "    > Ctrl+Shift+S : Abrir consola de depuracion.\n        \n"
)
DLG_TITLE_PATCH_NOTES = "Notas de la versión"
LBL_PATCH_NOTES = "CZT Mod Manager — Notas de la versión"
DLG_TITLE_UPDATE_ERROR = "Error de Actualizacion"
MSG_UPDATE_ERROR = "Error al descargar o ejecutar el instalador:\n{error}"
MSG_NO_RELEASE_NOTES = "No se encontraron notas de version para este canal de actualizacion."
MSG_RELEASE_NOTES_ERROR = "No se pudieron obtener las notas de version: {error}"

# ===== load_order.py =====
DLG_TITLE_LOAD_ORDER = "Orden de Carga"
MSG_LOAD_ORDER_NO_PROFILE = "No se pudo determinar el perfil actual."
MSG_LOAD_ORDER_NO_PROFILE_SET = "No hay perfil actual configurado."
MSG_LOAD_ORDER_PROFILE_NOT_FOUND = "No se encontro configuracion de perfil: {profile_name}"
MSG_LOAD_ORDER_MODS_DIR_MISSING = "El directorio de mods no existe para el perfil: {profile_name}"
DLG_TITLE_SET_LOAD_ORDER = "Establecer Orden de Carga - {profile_name}"
DLG_TITLE_LOAD_ORDER_BLOCKED = "Orden de Carga Bloqueado"
MSG_LOAD_ORDER_BLOCKED_PROFILE = "El menu de orden de carga esta desactivado para este perfil: {profile_name}"
LBL_LOAD_ORDER_TITLE = "Selecciona un mod y usa los controles de abajo para generar el archivo de orden de carga."
LBL_LOAD_ORDER_SUBTITLE = "> Haz clic en 'Guardar Orden' para aplicar cambios y luego iniciar el juego.\n> El orden de carga se mantiene hasta que lo cambies otra vez."
BTN_LOAD_ORDER_MOVE_UP = "Mover Arriba"
BTN_LOAD_ORDER_MOVE_DOWN = "Mover Abajo"
BTN_LOAD_ORDER_SAVE_ORDER = "Guardar Orden"
LBL_LOAD_ORDER_LEGEND_CONTROLS = "Controles:"
LBL_LOAD_ORDER_LEGEND_MOVE_UP = "Mover Arriba"
LBL_LOAD_ORDER_LEGEND_MOVE_DOWN = "Mover Abajo"
LBL_LOAD_ORDER_LEGEND_DRAG = "Arrastrar: Mover Arriba o Abajo"
LBL_LOAD_ORDER_LEGEND_SAVE = "Guardar: Establecer Orden de Carga"
DLG_TITLE_SAVE = "Guardar"
MSG_LOAD_ORDER_SAVED = "Orden de carga guardado correctamente."
DLG_TITLE_ERROR_SAVING = "Error al Guardar"
MSG_LOAD_ORDER_SAVE_FAILED = "Error al guardar el orden de carga:\n{error}"

# ===== plugins/F3_Menu.py =====
DLG_TITLE_PLUGIN_MANAGER = "Gestor de Plugins"
BTN_PLUGIN_MENU = "Plugins"
LBL_PLUGIN_MANAGER_INSTALLED = "Plugins instalados"
BTN_PLUGIN_MANAGER_RESCAN = "Reescanear"
MSG_PLUGIN_MANAGER_NOT_INITIALISED = "El gestor de plugins no esta inicializado."
MSG_PLUGIN_MANAGER_EMPTY = (
    "No se encontraron plugins.\n\n"
    "Coloca las carpetas de plugins en:\n  {plugins_root}\n\n"
    "Cada carpeta de plugin debe contener un manifiesto plugin.json."
)
CB_PLUGIN_ENABLE_PROFILE_FMT = "Perfil ({profile})"
LBL_PLUGIN_PROFILE_NONE = "ninguno"
BTN_PLUGIN_OPEN_FOLDER = "Abrir carpeta"
MSG_PLUGIN_MANAGER_SAVE_FAILED = "No se pudo guardar la configuracion:\n{error}"
MSG_PLUGIN_ROOT_NOT_SET = "La carpeta raiz de CZT no esta configurada. No se pueden cargar plugins."
LBL_PLUGIN_STANDALONE_EXE = "EXE Independiente:"
LBL_PLUGIN_SCRIPTS = "Scripts:"
LBL_PLUGIN_NONE_STANDALONE = "No se encontraron plugins EXE independientes."
LBL_PLUGIN_NONE_SCRIPTS = "No se encontraron plugins de script."
CB_PLUGIN_ENABLE_PROFILE = "Habilitar para Perfil"
CB_PLUGIN_ENABLE_GLOBAL = "Habilitar Globalmente"
CB_PLUGIN_RUN_STARTUP = "Ejecutar al Iniciar"
BTN_PLUGIN_RUN = "Ejecutar"
BTN_PLUGIN_UNLOAD = "Descargar"
BTN_PLUGIN_SAVE_STARTUP_OPTIONS = "Guardar Opciones de Inicio"
BTN_PLUGIN_CLOSE = "Cerrar"
DLG_TITLE_PLUGIN_RUN_AS_ADMIN = "¿Ejecutar como administrador? (opcional)"
MSG_PLUGIN_RUN_AS_ADMIN = "¿Quieres ejecutar {plugin_name} como administrador?"
DLG_TITLE_PLUGIN = "Plugin"
MSG_PLUGIN_LAUNCHED = "Iniciado: {plugin_name}"
DLG_TITLE_PLUGIN_ERROR = "Error de Plugin"
MSG_PLUGIN_LAUNCH_FAILED = "No se pudo iniciar el plugin:\n{error}"
MSG_PLUGIN_UNLOAD_FAILED = "No se pudo descargar el plugin:\n{error}"
MSG_PLUGIN_UNLOADED = "Descargado: {plugin_name}\n\nNota: Esto solo elimina el modulo de memoria.\nLos hilos, senales o elementos de UI pueden seguir activos si el plugin no se limpia por si mismo."
MSG_PLUGIN_NOTHING_TO_UNLOAD = "No hay nada para descargar de: {plugin_name}"
DLG_TITLE_PLUGIN_STARTUP_REQUIREMENTS = "Requisitos de Inicio no Cumplidos"
MSG_PLUGIN_STARTUP_REQUIREMENTS = "Los plugins marcados para iniciar deben estar habilitados Globalmente o para un Perfil.\nEstos plugins no se cargaran al inicio hasta corregirlo:\n- {plugins}"
DLG_TITLE_SAVED = "Guardado"
MSG_PLUGIN_OPTIONS_SAVED = "Opciones de plugin guardadas."
DLG_TITLE_SAVE_ERROR = "Error al Guardar"
MSG_PLUGIN_OPTIONS_SAVE_FAILED = "No se pudieron guardar las opciones del plugin:\n{error}"

# ===== popup_policies.py =====
POPUP_TITLE_CUSTOM_SETTINGS = "Ajustes Personalizados"
POPUP_TITLE_MANAGE_LOADOUTS = "Gestionar Loadouts"
POPUP_TITLE_FIRST_TIME_SETUP = "Configuracion Inicial"
POPUP_TITLE_RESTORE_BACKUP = "Restaurar Copia"
POPUP_TITLE_FORCE_UPDATE_OPTIONS = "Opciones de Actualizacion Forzada"
POPUP_TITLE_CLEAN_OPTIONS = "Opciones de Limpieza"

# ===== UserSetup_Actions.py =====
DLG_TITLE_NO_DRIVES = "Sin Unidades"
MSG_NO_DRIVES = "No se encontraron unidades disponibles."
DLG_TITLE_NO_ROOT_FOLDER = "Sin Carpeta Raiz"
MSG_NO_ROOT_FOLDER = "La carpeta raiz de CZT no esta configurada o no existe."
DLG_TITLE_ROOT_CREATED = "Raiz Creada"
MSG_ROOT_CREATED = "Carpetas raiz de CZT creadas en: {czt_root_folder}"
DLG_TITLE_SELECT_UNRAR = "Seleccionar Ejecutable de UnRAR"
MSG_UNRAR_INSTALLER_PROMPT = (
    "El instalador de UnRAR se iniciara a continuacion.\n"
    "Configura la carpeta de destino en:\n"
    " > Unidad_Seleccionada_Para_Raiz\\CZT Mod Manager\\czt_tools <"
)
LOG_UNRAR_INSTALLER_LAUNCHED = (
    "Instalador de UnRAR iniciado. Completa la instalacion.\n"
    " ¡La instalacion termina cuando finaliza el proceso de extraccion!"
)

# ===== backups/mod_backup.py =====
DLG_TITLE_CREATE_BACKUP = "Crear Copia de Seguridad"
MSG_BACKUP_ROOT_NOT_SET = "La carpeta raiz no esta configurada."
MSG_BACKUP_CHOOSE = "Elige que respaldar:"
BTN_BACKUP_MOD_FILES = "Solo Archivos de Mods"
BTN_BACKUP_MODS_LIST = "Solo mods_list.json"
BTN_BACKUP_FILES_AND_LIST = "Respaldo de Archivos + Lista"
MSG_BACKUP_SUCCESS = "Copia de seguridad creada correctamente.\n\n"
MSG_BACKUP_WARNINGS = "Copia de seguridad completada con advertencias.\n\n"
MSG_BACKUP_FAILED = "La copia de seguridad fallo.\n\n"

# ===== backups/restore_backup.py =====
DLG_TITLE_RESTORE_BACKUP = "Restaurar Copia de Seguridad"
MSG_RESTORE_ROOT_NOT_SET = "La carpeta raiz no esta configurada."
MSG_RESTORE_BACKUPS_NOT_FOUND = "No se encontro carpeta de copias: {backup_root}"
LBL_RESTORE_HEADER = "Selecciona carpetas de copia para restaurar o eliminar"
LBL_NO_BACKUPS = "No se encontraron copias"
LBL_BACKUP_META = "Contiene: {kind_text}   |   Creado: {stamp}"
MSG_RESTORE_SELECT_ONE = "Selecciona una copia para instalar."
MSG_RESTORE_ONLY_ONE = "Instalar admite exactamente una copia seleccionada a la vez."
MSG_RESTORE_SELECT_DELETE = "Selecciona una o mas copias para eliminar."
MSG_DELETE_SINGLE = "¿Eliminar copia '{name}'?"
MSG_DELETE_MULTIPLE = "¿Eliminar {count} carpetas de copia?\n\n{preview}{extra}"
DLG_TITLE_DELETE_BACKUP = "Eliminar Copia de Seguridad"
MSG_DELETE_ERRORS = "No se pudieron eliminar algunas carpetas de copia:\n\n"
BTN_INSTALL_SELECTED = "Instalar Seleccionada"
BTN_DELETE_SELECTED = "Eliminar Seleccionadas"
MSG_RESTORE_CONFIRM = "¿Restaurar copia '{backup_name}' para el perfil '{profile_name}'?"
MSG_RESTORE_CONFIRM_DETAIL = "Esto reemplazara archivos de mods activados/desactivados actuales, loadouts guardados y/o profile_mods_list.json."
MSG_RESTORE_SUCCESS = "Restauracion completada correctamente.\n\n"
MSG_RESTORE_WARNINGS = "Restauracion completada con advertencias.\n\n"
MSG_RESTORE_FAILED = "La restauracion fallo.\n\n"

# ===== install_mods/process_install.py =====
DLG_TITLE_NOTHING_SELECTED = "Nada seleccionado"
MSG_NO_MODS_SELECTED_INSTALL = "No se seleccionaron mods para instalar."
DLG_TITLE_CONFIRM_INSTALL = "Confirmar Instalacion"
MSG_CONFIRM_INSTALL_LIST = "¿Instalar los siguientes {count} mod(s)?\n\n{mod_list}"
MSG_CONFIRM_INSTALL_COUNT = "¿Instalar {count} mod(s) seleccionados?"
DLG_TITLE_ERROR = "Error"
MSG_NO_ROOT_FOLDER_INSTALL = "¡No hay carpeta raiz configurada! Haz clic en setup y crea una carpeta raiz antes de intentar instalar mods."
MSG_SELECTED_MODS_NOT_FOUND = "No se encontraron los archivos de mod seleccionados."
DLG_TITLE_CONFIRM_SOURCE_DELETE = "Confirmar Eliminacion del Origen"
MSG_CONFIRM_SOURCE_DELETE = "¿Eliminar archivo(s) de mod restantes de la carpeta de origen despues de instalar?\n\n{preview}{extra}"

# ===== install_mods/process_uninstall.py =====
MSG_NO_FILES_SELECTED_DELETE = "No se seleccionaron archivos para eliminar."
DLG_TITLE_CONFIRM_DELETE = "Confirmar Eliminacion"
MSG_CONFIRM_DELETE_COUNT = "¿Seguro que quieres eliminar {count} archivo(s)?"

# ===== install_mods/dying_light_auto_patch.py =====
DLG_TITLE_DL_DATA_SLOT = "Reemplazar Ranura de Datos de Dying Light"
LBL_DL_DATA_SLOT_CHOOSE = "Elige un archivo de datos existente de Dying Light para reemplazar antes de instalar, instalar como nuevo usando la siguiente ranura libre, o cancelar la instalacion."
LBL_DL_SOURCE_MOD = "Mod de Origen: {source_display}"
LBL_DL_INSTALLING = "Instalando: {incoming_file}"
LBL_DL_PROFILE = "Perfil: {profile_name}"
BTN_INSTALL_AS_NEW = "Instalar como Nuevo"
BTN_INSTALL_AS_NEW_SLOT = "Instalar como Nuevo ({target})"
BTN_CANCEL_INSTALL = "Cancelar Instalacion"
LBL_DL_STATE_ACTIVE = "Activo"
LBL_DL_STATE_DISABLED = "Desactivado"

# ===== install_mods/archive_handler/archive_handler_core.py =====
DLG_TITLE_ARCHIVE_INSTALL_CHOICE = "Opcion de Instalacion de Archivo"
MSG_ARCHIVE_MULTI_CANDIDATES = "Se encontraron multiples candidatos de instalacion en el archivo:\n{archive_title}\n\nExtensiones permitidas para este perfil: {exts_label}\nSelecciona un candidato para instalar, instala todos o omite este archivo."
BTN_INSTALL_ALL = "Instalar Todo"
BTN_SKIP_ARCHIVE = "Omitir Este Archivo"
DLG_TITLE_SELECTION_REQUIRED = "Seleccion Requerida"
MSG_SELECT_CANDIDATE_FIRST = "Selecciona primero un candidato, o usa Instalar Todo."
DLG_TITLE_ARCHIVE_FOLDER_CHOICE = "Opcion de Carpeta del Archivo"
MSG_ARCHIVE_MULTI_FOLDERS = "Se encontraron multiples candidatos de carpeta en el archivo:\n{archive_title}\n\nSelecciona una carpeta candidata para instalar, instala todas o omite este archivo."

# ===== install_mods/replacement_handler/resolve_replacement.py =====
DLG_TITLE_SELECT_REPLACEMENT = "Seleccionar Destino de Reemplazo"
MSG_REPLACEMENT_DEFAULT = "Se encontraron archivos coincidentes/similares. Elige que archivo reemplazar o omite el reemplazo."
BTN_SKIP_REPLACEMENT = "Omitir Reemplazo (Instalar Archivo Nuevo/Reemplazar Coincidencia Exacta)"

# ===== launch_game/launcher_core.py =====
MSG_NO_INSTALL_DIR = (
    "¡No hay un directorio de instalacion valido configurado!\n \n- Modo de Ruta [STEAM]:\n   > Haz clic en 'Detect Steam'\n "
    "\n- Modo de Ruta [Manual]:\n   > Haz clic en 'SET INSTALL' y 'SET EXE' para configurar."
)
MSG_EXE_NOT_FOUND = "¡No se pudo encontrar el EXE para {game_name}!\n"
DLG_TITLE_CZT_LAUNCHER = "Lanzador CZT"
MSG_LAUNCH_OPTIONS = (
    "Opciones de inicio de {game_name}: \n\n"
    " ➡️ Link | Modded = Enlazar mods activados.\n"
    " ➡️ Unlink | Safe = Eliminar enlaces existentes.\n"
    " ➡️ Cancel = ¡Abortar lanzamiento de misil!"
)
BTN_LINK_MODDED = "Link | Modded"
BTN_UNLINK_SAFE = "Unlink | Safe"
MSG_ELEVATION_REQUIRED = "Se requieren privilegios elevados. Intentando reiniciar como admin.\n\nError: {error}"
MSG_PERMISSION_DENIED = "Permiso denegado.\n\nError: {error}"
MSG_LAUNCH_TOGGLE_FAILED = "No se pudieron alternar mods o iniciar el juego:\n{error}"

# ===== launch_game/launcher_utilities.py =====
MSG_ELEVATION_FAILED = "Error al elevar a admin: {error}"
MSG_SYMLINK_PERMISSIONS = (
    "Windows requiere permisos de Admin para crear symlinks.\n\n"
    "Elige una opcion:\n"
    "- Ejecutar la aplicacion como Administrador.\n"
    "- Habilitar Modo Desarrollador en la configuracion de Windows para evitarlo permanentemente.\n"
    "    ↳ ¡No se requieren permisos de admin!\n"
)
BTN_RUN_AS_ADMIN = "Ejecutar como Administrador"
BTN_OPEN_WIN_SETTINGS = "Abrir Configuracion de Windows"
MSG_DEV_MODE_OPEN_FAILED = "No se pudo abrir la configuracion de Modo Desarrollador."

# ===== launch_game/log_messages.py =====
LOG_AUDIO_MENU_MUSIC_PAUSED = "[AUDIO] Musica del menu pausada. Reinicia CZT para restablecerla, o vuelve a guardar los ajustes de audio para reanudar."
LOG_LAUNCH_LOAD_ORDER_READ_FAILED = "[LAUNCH] No se pudo leer el orden de carga: {error}"
LOG_CONFIG_RELOAD_FAILED = "[ERROR] No se pudo recargar la configuracion desde disco: {error}"
LOG_LAUNCH_SEARCHING_EXE = "[FIRST TIME LAUNCH]\n- Buscando EXE en: {steam_libraries}"
LOG_LAUNCH_EXE_NOT_FOUND = "[ERROR] No se pudo encontrar el EXE para {game_name}!"
LOG_NO_ROOT_SET = "[ERROR] No hay carpeta raiz configurada. Haz clic en 'CREATE ROOT' para empezar a usar CZT."
LOG_LAUNCH_CREATED_MODS_FOLDER = "[LAUNCH] Se creo la carpeta de mods faltante: {path}"
LOG_LAUNCH_CREATED_MODS_FOLDER_PARENT = "[LAUNCH] Se creo la carpeta padre de mods faltante: {path}"
LOG_MODS_FOLDER_PREP_FAILED = "[ERROR] No se pudo preparar la ruta de carpeta de mods {path}: {error}"
LOG_LAUNCH_CANCELLED = "[LAUNCH] Lanzamiento de {game_name} cancelado por el usuario!"
LOG_TOTAL_LINKED = "[TOTAL] {count} mod(s) enlazados"
LOG_PER_FILE_REMOVE_FAILED = "[PER-FILE] No se pudo eliminar el symlink {path}: {error}"
LOG_TYPE_SYMLINKS_REMOVED = "[{mod_type}] {count} symlink(s) eliminados"
LOG_PER_FOLDER_REMOVE_FAILED = "[PER-FOLDER] No se pudo eliminar symlink/junction {path}: {error}"
LOG_PER_FOLDER_REMOVED_COUNT = "[PER-FOLDER] {count} symlink(s)/junction(s) eliminados"
LOG_LINK_DISABLED_MODS_JUNCTION = "[LINK] Junction de Mods desactivado: {path}"
LOG_LINK_DISABLED_MODS_SYMLINK = "[LINK] Symlink de Mods desactivado: {path}"
LOG_LINK_REMOVE_MODS_SYMLINK_FAILED = "[LINK] No se pudo eliminar el symlink de Mods: {error}"
LOG_LAUNCH_STEAM_START = "[LAUNCH] Steam esta iniciando app ID: {steam_appid} > {game_name} > {mode}"
LOG_STEAM_LAUNCH_FAILED_FALLBACK = "[ERROR] No se pudo iniciar con Steam: {error}\nVolviendo a inicio por EXE."
LOG_LAUNCH_STARTED_GAME = "[LAUNCH] Juego iniciado: {exe_path} {mode}"
LOG_ELEVATION_REQUIRED_RELAUNCH = "[ERROR] Se requiere elevacion: {error}\nIntentando reiniciar como admin..."
LOG_PERMISSION_DENIED_SIMPLE = "[ERROR] Permiso denegado: {error}"
LOG_LAUNCH_TOGGLE_FAILED_SIMPLE = "[ERROR] No se pudieron alternar mods o iniciar el juego: {error}"
LOG_TYPE_LINKING_TO = "[{mod_type}] Enlazando {count} mod(s) a {destination}"
LOG_MOD_LIST_ITEM = "  - {mod_name}"
LOG_LINK_MODS_DIR_MISSING = "[LINK] Carpeta de mods no encontrada o desactivada: {path}"
LOG_LINK_EXE_FAILED = "[LINK] No se pudo enlazar {file_name} al directorio del exe: {error}"
LOG_LINK_MODS_FOLDER_NOT_EMPTY = "[LINK] No se puede reemplazar la carpeta de mods porque no esta vacia: {path}"
LOG_LINK_PREP_MODS_FOLDER_FAILED = "[LINK] No se pudo preparar la carpeta de Mods para junction: {error}"
LOG_LINK_ENABLED_MODS_SUMMARY = "[LINK] Mods habilitados: \n - Origen: {source}\n - Enlazado a -> {destination}"
LOG_PER_FILE_CLEAN_FAILED = "[PER-FILE] Error al limpiar {path}: {error}"
LOG_PER_FILE_LINK_FAILED = "[PER-FILE] Error al enlazar {file_name}: {error}"
LOG_CONTENT_GAME_DIR_NOT_FOUND = "[CONTENT MOD] Directorio Content del juego no encontrado: {path}"
LOG_CONTENT_BACKUP_FAILED = "{tag} No se pudo respaldar {path}, omitiendo: {error}"
LOG_CONTENT_LINK_FAILED = "{tag} Error al enlazar {file_name}: {error}"
LOG_CONTENT_SKIP_JUNCTION_REAL_DIR = "{tag} Omitiendo junction, existe directorio real: {sub_name}"
LOG_CONTENT_JUNCTION_FAILED = "{tag} Error al crear junction {sub_name}: {error}"
LOG_PER_FOLDER_CLEAN_FAILED = "[PER-FOLDER] Error al limpiar {path}: {error}"
LOG_PER_FOLDER_LINKED_COUNT = "[PER-FOLDER] Se enlazaron {count} carpeta(s) -> {destination}"
LOG_IS_JUNCTION_FAILED = "[ERROR] is_junction fallo: {error}"
LOG_RMDIR_FAILED = "[ERROR] rmdir fallo para {link}: {error}"
LOG_REMOVE_FILE_LINK_FAILED = "[ERROR] Error al eliminar enlace de archivo: {link} - {error}"
LOG_REMOVE_JUNCTION_EXCEPTION = "[ERROR] Excepcion en remove_junction para {link}: {error}"
LOG_LAUNCH_REFRESHING_SYMLINKS = "[LAUNCH] Actualizando symlinks..."
LOG_ASI_DLL_REMOVE_FAILED = "[ASI_DLL] No se pudo eliminar symlink asi/dll {path}: {error}"
LOG_CONTENT_GAME_DIR_NOT_FOUND_SKIP_UNLINK = "[CONTENT MOD] game_content_dir no encontrado, omitiendo unlink: {path}"
LOG_CONTENT_UNLINK_FAILED = "{tag} Error al quitar enlace {path}: {error}"
LOG_CONTENT_RESTORE_FAILED = "{tag} Error al restaurar {path}: {error}"
LOG_CONTENT_UNLINKED_COUNT = "{tag} Se desenlazaron {count} mod(s)"
LOG_CONTENT_ORPHAN_REMOVED = "[CONTENT MOD] Se eliminaron {count} enlace(s) huerfano(s) (safety sweep)"
LOG_CONTENT_PRESERVE_DIR_CREATED = "[CONTENT MOD] Carpeta requerida recreada: {path}"
LOG_CONTENT_PRESERVE_DIR_FAILED = "[CONTENT MOD] No se pudo asegurar la carpeta requerida {path}: {error}"
LOG_LINK_DISABLED_FOLDER_JUNCTION = "[LINK] Junction de carpeta desactivado: {path}"
LOG_LINK_DISABLED_FOLDER_SYMLINK = "[LINK] Symlink de carpeta desactivado: {path}"
LOG_LINK_REMOVE_FOLDER_FAILED = "[LINK] Error al eliminar enlace de carpeta {path}: {error}"
LOG_LINK_DISABLED_FILE_SYMLINK = "[LINK] Symlink de archivo desactivado: {path}"
LOG_LINK_REMOVED_FILE = "[LINK] Archivo eliminado: {path}"
LOG_LINK_REMOVE_FILE_FAILED = "[LINK] Error al eliminar enlace de archivo {path}: {error}"
LOG_ELEVATION_FAILED_SIMPLE = "[ERROR] Error de elevacion: {error}"
LOG_DEV_MODE_SETTINGS_OPEN_FAILED = "[ERROR] No se pudo abrir configuracion de Modo Desarrollador: {error}"

# ===== install_mods/archive_handler/archive_handler_core.py logs =====
LOG_INSTALL_CONTENT_ADDED_MOD = "[{mod_type}] Mod agregado: {mod_label}"
LOG_INSTALL_CONTENT_ADDED_FOLDER_MOD = "[{mod_type}] Mod de carpeta agregado: {mod_name}"
LOG_COPY_CONTENT_MOD_FOLDER_FAILED = "[ERROR] copy_content_mod_folder fallo: {error}"
LOG_INSTALL_FILE_FAILED = "[ERROR] Ocurrio un error instalando {install_name}: {error}"

# ===== loadout_system/detect_missing.py =====
DLG_TITLE_MISSING_MODS = "Mods Faltantes"
MSG_MISSING_NO_LOADOUTS = "No se encontraron loadouts guardados para el perfil '{profile_name}'."
MSG_MISSING_LOADOUT_NOT_FOUND = "No se encontro el loadout '{target_loadout}'."
DLG_TITLE_DETECT_MISSING = "Detectar Mods Faltantes"
LBL_DETECT_MISSING_SELECT = "Selecciona un loadout para comparar contra los archivos instalados:"
MSG_MISSING_NO_FILES = "El loadout '{target_loadout}' no tiene archivos."
MSG_MISSING_NONE_DETECTED = "No se detectaron archivos faltantes para el loadout '{target_loadout}'."
MSG_MISSING_FOUND = "Se encontraron {count} archivo(s) de mod faltante(s) para el loadout '{target_loadout}'."
MSG_MISSING_DOWNLOAD_PROMPT = (
    "Se encontraron {count} archivo(s) de mod faltante(s) para '{target_loadout}'.\n\n"
    "¿Descargar e instalar ahora {download_count} elemento(s) faltante(s) con metadatos guardados del loadout?"
)
MSG_MISSING_NO_METADATA = "{count} elemento(s) faltante(s) no tienen metadatos de Nexus y se listaran en su lugar."

# ===== loadout_system/ls_ui_dropdown.py =====
BTN_LOADOUTS = "Loadouts"
TIP_LOADOUTS = (
    "1.) Empieza desactivando todos tus mods, luego activa los mods que quieres para el nuevo loadout.\n"
    "2.) Haz clic en el icono de guardar para guardar los mods activados como un archivo de loadout.\n"
    " - Los loadouts guardados se pueden cambiar desde este desplegable en cualquier momento.\n"
    " - En Gestionar Todo, cada fila de loadout tiene iconos de renombrar, copiar archivo y descargar.\n"
    " - Usa 'Importar desde archivo' para agregar loadouts desde otro archivo JSON.\n"
    " - Tambien puedes eliminar/editar informacion del loadout haciendo clic en 'Gestionar Todo'."
)

# ===== loadout_system/ls_ui_widgets.py =====
TIP_LOADOUT_CHECKBOX = "Marca para incluir este loadout al usar 'Cargar' o 'Combinar' Loadout."
TIP_RENAME_LOADOUT = "Renombrar loadout"
TIP_COPY_FILE = "Copiar archivo al portapapeles"
TIP_DOWNLOAD_LOADOUT = "Descargar este loadout"
TIP_DETECT_MISSING = (
    "¿Borraste accidentalmente un mod?\n"
    "Ejecuta esto para detectar y descargar mods faltantes de este loadout"
)
TIP_REFRESH_NEXUS = (
    "Validar y actualizar enlaces de nexus + IDs de archivo.\n"
    "Cuando un mod se actualiza en nexus, cambia el ID de descarga de archivos, pero el ID anterior puede seguir en el archivo de loadout.\n"
    "   - URLs/IDs obsoletos pueden provocar fallos de descarga.\n"
    "Al ejecutar esto, se revisaran esas entradas obsoletas y se actualizaran con la info mas reciente de Nexus.\n"
    "Ejecuta esto si,\n"
    "   - Has actualizado mods existentes recientemente (no agregados/eliminados, solo actualizados)\n"
    "   - Antes de compartir el loadout con otros."
)

# ===== loadout_system/ls_ui_manage_dialog.py =====
LBL_MANAGE_LOADOUTS_TITLE = "Archivos de Loadout:"
LBL_MANAGE_LOADOUTS_DESC = "(escribe un nombre abajo y luego haz clic en 'Guardar Loadout' para crear uno nuevo)"
LBL_MANAGE_LOADOUTS_TIP_1 = "Tip 1: Selecciona un loadout guardado y haz clic en 'Guardar Loadout' para sobrescribirlo."
LBL_MANAGE_LOADOUTS_TIP_2 = "Tip 2: Pasa el cursor sobre los botones para ver tooltips informativos."
LBL_CREATE_LOADOUT = "Crear Loadout:"
BTN_SAVE_LOADOUT = "Guardar Loadout"
BTN_LOAD_SELECTED = "Cargar Seleccionado"
BTN_MERGE_SELECTED = "Combinar Seleccionados"
BTN_IMPORT_LOADOUT = "Importar Loadout"
BTN_DELETE_LOADOUT = "Eliminar Loadout"

TIP_OPEN_LOADOUTS_FOLDER = "Abrir carpeta de loadouts"
TIP_SAVE_LOADOUT = (
    "- Ingresa un nuevo nombre y haz clic en 'Save Loadout' para crear un nuevo loadout \n"
    "- Selecciona un loadout existente y luego haz clic en 'Save Loadout' para sobrescribirlo"
)
TIP_LOAD_LOADOUT = (
    "Cargar (activar) uno o mas loadouts.\n"
    " Solo mods activados que esten instalados actualmente.\n"
    " Usa el boton de descarga para descargar realmente los archivos de lista de mods. \n"
    " Tambien puedes cargar un loadout y luego presionar F9 para detectar archivos de mod faltantes."
)
TIP_MERGE_LOADOUT = "Combinar loadouts seleccionados en un nuevo loadout."
TIP_IMPORT_LOADOUT = "Importar loadouts desde archivo JSON."
TIP_DELETE_LOADOUT = "Eliminar loadout seleccionado."
DLG_TITLE_OVERWRITE_LOADOUT = "Sobrescribir Loadout"
MSG_OVERWRITE_LOADOUT = "¿Sobrescribir loadout existente '{name}'?"
DLG_TITLE_COPY_LOADOUT = "Copiar Archivo de Loadout"
DLG_TITLE_DOWNLOAD_LOADOUT = "Descargar Loadout"
DLG_TITLE_REFRESH_NEXUS = "Actualizar Metadatos de Nexus"
MSG_NEXUS_API_REQUIRED = "Se requiere clave API de Nexus."
MSG_REFRESH_NEXUS_CONFIRM = "¿Validar enlaces de Nexus e IDs de archivo fijados para '{loadout_name}' y sobrescribir este archivo de loadout con metadatos actualizados?"
MSG_REFRESH_NO_ENTRIES = "Este loadout no tiene entradas de metadatos. Guarda o importa metadatos primero."
MSG_REFRESH_WRITE_ERROR = "La validacion termino, pero no se pudo escribir el archivo:\n{error}"
MSG_REFRESH_COMPLETE = (
    "Actualizacion completada para '{loadout_name}'.\n\n"
    "Escaneados: {scanned_count}\n"
    "Validos: {valid_count}\n"
    "Invalidos: {invalid_count}\n"
    "IDs muertos reparados: {repaired_count}\n"
    "Entradas actualizadas (total): {changed}\n"
)
DLG_TITLE_LOADOUTS = "Loadouts"
MSG_MULTI_SELECT_ONLY_DELETE = "Solo hay acciones de eliminacion disponibles cuando se seleccionan multiples elementos.\n\nAccion solicitada: {action_label}"
MSG_OVERWRITE_PIN_MODE = "¿Sobrescribir loadout existente '{name}' con los mods actualmente activados?\n\nElige como manejar la seleccion de ID de archivo para mods en este loadout:\n\n"
BTN_UPDATE_ALL = "Actualizar Todo"
BTN_UPDATE_NEW = "Actualizar Nuevos"
BTN_DONT_UPDATE = "No Actualizar"
MSG_SELECT_ONE_OVERWRITE = "Selecciona solo un loadout para sobrescribir o ingresa un nombre nuevo."
MSG_ENTER_LOADOUT_NAME = "Ingresa un nombre de loadout o selecciona uno para sobrescribir."
DLG_TITLE_SAVE_LOADOUT = "Guardar Loadout"
MSG_PIN_FILE_IDS_PROMPT = (
    "Algunos mods tienen multiples archivos principales u opcionales disponibles en Nexus.\n"
    "¿Quieres guardar la version especifica del archivo en este loadout?\n\n"
    "Hacer esto ahora hara que descargar/compartir el loadout sea mas consistente en el futuro.\n\n"
    "Nota: CZT te mostrara cada variante disponible para una seleccion facil. No necesitas buscar manualmente.\n"
)
MSG_OVERWRITE_SAVED = "Sobrescritura guardada.\n\nModo usado: {mode_label}\nIDs de archivo actualizados: {processed}"
MSG_OVERWRITE_SAVED_NO_CHANGE = "Sobrescritura guardada.\n\nModo usado: {mode_label}\n0 entradas actualizadas. Los datos nuevos coincidieron con los existentes."
MSG_SELECT_LOADOUTS_DELETE = "Selecciona uno o mas loadouts guardados para eliminar."
DLG_TITLE_DELETE_LOADOUTS = "Eliminar Loadouts"
MSG_CHECK_LOADOUTS_LOAD = "Marca uno o mas loadouts guardados para cargar."
DLG_TITLE_LOAD_LOADOUT = "Cargar Loadout"
MSG_LOADED_LOADOUTS = "Se cargaron {count} loadout{plural} correctamente."
DLG_TITLE_MERGE_LOADOUTS = "Combinar Loadouts"
MSG_SELECT_TWO_MERGE = "Selecciona al menos dos loadouts guardados para combinar."
LBL_MERGED_LOADOUT_NAME = "Nombre del loadout combinado:"
MSG_ENTER_MERGED_NAME = "Ingresa un nombre valido para el loadout combinado."
DLG_TITLE_RENAME_LOADOUT = "Renombrar Loadout"
LBL_NEW_FILE_NAME = "Nombre de archivo nuevo:"

# ===== loadout_system/download_list.py =====
DLG_TITLE_DOWNLOAD_MOD_LIST = "Descargar Lista de Mods"
MSG_RUN_INSTALL_NOW = "{summary_text}\n\n¿Ejecutar instalacion ahora?"
MSG_INSTALL_NOT_AVAILABLE = "Logica de instalacion no disponible"

# ===== loadout_system/importing.py =====
DLG_TITLE_IMPORT_LOADOUTS = "Importar Loadouts"
MSG_IMPORT_ROOT_NOT_SET = "La carpeta raiz no esta configurada."

# ===== nexus/updates.py =====
MSG_API_KEY_REQUIRED = (
    "Se requiere tu clave API de Nexus para comprobar actualizaciones.\n"
    "La clave API se usa para comunicarse con el sitio de Nexus.\n"
    " La clave se guarda localmente dentro de tu archivo de configuracion."
)
MSG_NO_TRACKED_MODS = "No se encontraron mods rastreados para este perfil."
MSG_ALL_UP_TO_DATE = "¡Todos los mods estan actualizados!"
LBL_UPDATES_AVAILABLE = "Actualizaciones disponibles:"
UPDATE_LINE_FMT = "→ {mod_name} (Actual: {local_version} | Nuevo: {latest_version})"

# ===== nexus/nexus_sync.py =====
MSG_MOD_DIR_NOT_SET = (
    "El directorio de mods no esta configurado o no existe. "
    "Configura tu directorio de mods en la pestaña User Settings antes de guardar enlaces de Nexus."
)
MSG_NEXUS_INFO_UPDATED = "Informacion de Nexus actualizada para {count} mod(s)."

# ===== nexus/downloads.py =====
LBL_SELECT_FILE_DOWNLOAD = "Seleccionar archivo para descargar"
LBL_SELECT_A_FILE = "Selecciona un archivo para descargar..."
BTN_DOWNLOAD = "Descargar"
BTN_CANCEL = "Cancelar"
ERR_DOWNLOAD_CANCELLED = "Descarga cancelada"
ERR_NO_FILE_SELECTED = "No se selecciono archivo"
ERR_MISSING_API_KEY = "Falta la clave API de Nexus"
ERR_NO_FILES_AVAILABLE = "No hay archivos disponibles"
ERR_MISSING_MOD_ID_URL = "Falta Nexus Mod ID o URL"
ERR_CANNOT_RESOLVE_SLUG = "No se puede resolver el slug de juego de Nexus para este perfil"
ERR_INVALID_MOD_ID_URL = "Nexus Mod ID o URL invalido"
ERR_NO_DOWNLOADABLE_FILE = "No hay id de archivo descargable"
ERR_MISSING_ROOT_FOLDER = "Falta czt_root_folder"
ERR_NO_SELECTED_MODS = "No hay mods seleccionados"
ERR_NO_TRACKED_MODS_PROFILE = "No hay mods rastreados para el perfil actual"
ERR_NO_VALID_NEXUS_URL = "No hay mods seleccionados con nexus_url valido"
LBL_INSTALLED_MOD = "Mod Instalado: {name}"
LBL_INSTALLED_FILE = "Archivo Instalado: {name}"
LBL_FILE_UNKNOWN = "Desconocido"
LBL_FILE_VERSION = "Version {version}"

# ===== nexus/browse_mods/browser_actions.py =====
MSG_OPEN_MOD_PAGE_FIRST = (
    "Abre primero una pagina especifica de mod en Nexus y luego haz clic en Add Current Mod.\n\n"
    "Formato de URL esperado:\n"
    "https://www.nexusmods.com/<game>/mods/<id>"
)
STATUS_DOWNLOADING_MOD = "Descargando mod {mod_id}..."
STATUS_DOWNLOAD_FAILED = "Descarga fallida"
STATUS_DOWNLOAD_INSTALLING = "Descarga completa. Instalando..."
STATUS_DOWNLOADED = "Descargado: {name}"
MSG_DOWNLOAD_COMPLETE_SAVED = "Descarga completa.\n\nGuardado en: {path}"
STATUS_INSTALL_FAILED = "Instalacion fallida"
STATUS_INSTALLED = "Instalado: {name}"

# ===== nexus/browse_mods/browser_widgets.py =====
LBL_SELECT_A_MOD = "Selecciona un mod"
LBL_NOT_INSTALLED = "No Instalado"
BTN_ADD_TO_FAVORITES = "Agregar a Favoritos"
LBL_ZERO_DOWNLOADS = "0 descargas"
LBL_ZERO_ENDORSEMENTS = "0 apoyos"
LBL_UPDATED_NONE = "Actualizado: --"
LBL_NO_MOD_SELECTED = "Ningun mod seleccionado"
LBL_PAK_FILES = "Archivos Pak"
LBL_NO_FILES_AVAILABLE = "No hay archivos disponibles"
LBL_NO_CHANGELOG = "No hay registro de cambios disponible"
LBL_UNKNOWN_MOD = "Mod Desconocido"
LBL_BY_AUTHOR = "Por {author}"
LBL_DOWNLOADS_COUNT = "{count} descargas"
LBL_ENDORSEMENTS_COUNT = "{count} apoyos"
LBL_UPDATED_DATE = "Actualizado {date}"
LBL_NO_DESCRIPTION = "No hay descripcion disponible."

# ===== nexus/browse_mods/browser_window.py =====
DLG_TITLE_BROWSE_NEXUS = "Explorar Nexus Mods - {profile}"
TIP_BACK = "Atras"
TIP_FORWARD = "Adelante"
TIP_REFRESH = "Actualizar"
TIP_GO = "Ir"
TIP_ENDORSEMENT_STATUS = "Estado de apoyo"
MSG_WEBENGINE_UNAVAILABLE = (
    "Qt WebEngine no esta disponible en esta instalacion.\n"
    "Instala PySide6-WebEngine para habilitar la navegacion de Nexus dentro de la app."
)
STATUS_BROWSER_UNAVAILABLE = "Navegador integrado no disponible"
STATUS_LOADING_PAGE = "Cargando pagina..."
STATUS_NO_NEXUS_LINK = "No hay enlace de juego de Nexus configurado para este perfil"
STATUS_LOADING_MODS = "Cargando mods de Nexus..."
STATUS_PAGE_LOADED = "Pagina cargada"
STATUS_PAGE_FAILED = "Error al cargar pagina"

# ===== nexus/browse_mods/endorsements.py =====
TIP_ENDORSE_ONLY_MOD_PAGES = "El estado de apoyo solo esta disponible en paginas de mods"
TIP_ENDORSED = "Apoyado"
TIP_NOT_ENDORSED = "No apoyado"
ERR_INVALID_ENDORSEMENT = "Accion de apoyo invalida"
ERR_UNKNOWN_ENDORSEMENT = "Error de apoyo desconocido"
STATUS_OPEN_MOD_TO_ENDORSE = "Abre una pagina de mod especifica para apoyar"
STATUS_ENDORSE_UNAVAILABLE = "Estado de apoyo no disponible"
STATUS_UPDATING_ENDORSEMENT = "Actualizando apoyo..."
STATUS_ENDORSED = "Apoyado"
STATUS_ENDORSEMENT_REMOVED = "Apoyo eliminado"
STATUS_ENDORSEMENT_FAILED = "Fallo al apoyar"
MSG_ENDORSEMENT_FAILED = "No se pudo actualizar el apoyo.\n\n{error}"

# ===== nexus/browse_mods/install_state.py =====
LBL_MOD_INSTALLED = "Mod instalado"
LBL_MOD_NOT_INSTALLED = "Mod no instalado"

# ===== nexus/protocol_handler/nxm/nxm_actions.py =====
MSG_NXM_GAME_MISMATCH = (
    "Este mod es para \"{game}\". \n"
    "El perfil actual es \"{profile}\".\n\n"
    "Cambia al perfil \"{game}\" e intentalo de nuevo."
)

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py =====
MSG_CZTMM_GAME_MISMATCH = (
    "El mod que intentaste instalar es para \"{game}\". \n"
    "Tu perfil actual es \"{profile}\".\n\n"
    "Cambia al perfil \"{game}\" e intentalo de nuevo."
)

# ===== refresh_manager/refresh_manager.py =====
PLACEHOLDER_SEARCH_MODS = "Buscar mods : {profile}"


# =====================================================================
#  MENSAJES DE REGISTRO (czt_log / czt_log_synced)
# =====================================================================

# ===== install_mods/process_install.py (logs) =====
LOG_INSTALL_CANCELLED = "[INSTALL CANCELLED] Instalacion cancelada por el usuario durante la confirmacion de reemplazo."
LOG_INSTALL_FAILED = "\n[ERROR] La instalacion fallo: {error}\n"
LOG_INSTALL_QUEUED = "[INSTALL] Otra instalacion esta en ejecucion. Encolando esta solicitud de instalacion."
LOG_INSTALL_SELECTED_FILES = "\n[INSTALL] Archivos Seleccionados:\n{file_list}"
LOG_PROCESSING_MOD = "[PROCESSING] Mod: {install_label}"
LOG_INSTALL_MOD_FAILED = "[ERROR] Fallo al instalar '{install_label}': {error}"
LOG_DELETE_SOURCE_FAILED = "[DELETE AFTER INSTALLED] Error al eliminar elemento de origen '{src_path}': {error}"
LOG_INSTALL_COMPLETED = " \n[INSTALL PROCESS COMPLETED] Todos los mods seleccionados han sido procesados.\n"
LOG_SUMMARY = "[SUMMARY]"
LOG_SUMMARY_SUCCESS = "\n    > EXITO: "
LOG_SUMMARY_FAILED = "\n    > FALLIDO: "
LOG_SUMMARY_SKIPPED = "\n    > OMITIDO: (no se encontro candidato de archivo coincidente con exporter) "
LOG_SUMMARY_SOURCE_DELETED = "\n    > ARCHIVO ORIGEN ELIMINADO: "
LOG_SUMMARY_SOURCE_DELETE_SKIPPED = "\n    > ELIMINACION DE ARCHIVO ORIGEN OMITIDA: el usuario rechazo la confirmacion."

# ===== install_mods/process_uninstall.py (logs) =====
LOG_DELETED_MODS = "[DELETE] Se eliminaron {count} mod(s):\n -> {item_list}"

# ===== install_mods/dying_light_auto_patch.py (logs) =====
LOG_DL_SLOT_SKIPPED = "[DL DATA SLOT] Se omitio '{base_name}' porque no se selecciono un destino de reemplazo y su ranura actual no esta disponible."
LOG_DL_SLOT_KEEP = "[DL DATA SLOT] Manteniendo nombre de archivo entrante '{base_name}' para instalar."
LOG_DL_SLOT_INSTALL_NEW = "[DL DATA SLOT] Instalar como nuevo selecciono la siguiente ranura disponible '{selected_file_name}' para '{base_name}'."
LOG_DL_SLOT_REPLACE = "[DL DATA SLOT] Se selecciono destino de reemplazo '{selected_file_name}' para '{base_name}'."

# ===== install_mods/archive_handler/archive_handler_core.py (logs) =====
LOG_OPTION_SKIP_NO_EXPORTERS = "[INSTALL][OPTION][SKIPPED] No hay nombres base de exporter disponibles para candidatos de {choice_kind} en {archive_name}."
LOG_OPTION_AUTO_SELECT = "[INSTALL][OPTION] Se seleccionaron automaticamente {count} candidato(s) de {choice_kind} coincidentes con exporter en {archive_name}."
LOG_OPTION_SKIP_NO_MATCH = "[INSTALL][OPTION][SKIPPED] No se encontraron candidatos de {choice_kind} coincidentes con exporter en {archive_name}."
LOG_CACHE_SKIP = "[INSTALL][OPTION][CACHE] Se uso opcion de archivo en cache: omitir archivo {archive_name}"
LOG_CACHE_INSTALL_ALL = "[INSTALL][OPTION][CACHE] Se uso opcion de archivo en cache: instalar todo desde archivo {archive_name}"
LOG_CACHE_SELECTED = "[INSTALL][OPTION][CACHE] Se uso seleccion de archivo en cache: {chosen_rel}"
LOG_MULTI_FOLDER_CANDIDATES = "[INSTALL][OPTION] Se encontraron multiples candidatos de carpeta en archivo: {archive_name}"
LOG_SKIPPED_FOLDER_CHOICE = "[INSTALL][SKIPPED] El usuario omitio opcion de carpeta de archivo: {archive_name}"
LOG_ADDITIONAL_FOLDER_CANDIDATES = "[INSTALL][OPTION] Se encontraron candidatos de carpeta adicionales en la opcion seleccionada: {archive_name}"
LOG_SKIPPED_NESTED_FOLDER = "[INSTALL][SKIPPED] El usuario omitio opcion de carpeta anidada: {archive_name}"
LOG_MULTI_FILE_CANDIDATES = "[INSTALL][OPTION] Se encontraron multiples candidatos de instalacion en archivo: {archive_name}"
LOG_SKIPPED_FILE_CHOICE = "[INSTALL][SKIPPED] El usuario omitio opcion de instalacion de archivo: {archive_name}"
LOG_ADDITIONAL_FILE_CANDIDATES = "[INSTALL][OPTION] Se encontraron candidatos de archivo adicionales en la opcion seleccionada: {archive_name}"
LOG_SKIPPED_NESTED_FILE = "[INSTALL][SKIPPED] El usuario omitio opcion de archivo anidado: {archive_name}"
LOG_UNSUPPORTED_ARCHIVE = "[ERROR] Tipo de archivo no compatible o libreria faltante: {archive_type}"
LOG_RAR_NOT_AVAILABLE = "[ERROR] Libreria rarfile no disponible para extraccion .rar: {archive_name}."
LOG_7Z_NOT_AVAILABLE = "[ERROR] Libreria py7zr no disponible para extraccion .7z: {archive_name}"
LOG_PROCESS_ITEM_FAILED = "[ERROR] Error al procesar {item}: {error}"
LOG_EXTRACT_FAILED = "[ERROR] Error al extraer {archive_type} {archive_name}: {error}"

# ===== install_mods/replacement_handler/resolve_replacement.py (logs) =====
LOG_REPLACEMENT_CONFIRM = "[INSTALL SAFETY] Se requiere confirmacion de reemplazo para '{mod_name}'"
LOG_REPLACEMENT_REMOVE_FAILED = "[WARN] No se pudo eliminar el archivo de reemplazo seleccionado '{old_path}': {error}"
LOG_REPLACEMENT_DIALOG_FAILED = "[WARN] La ventana de confirmacion de reemplazo fallo: {error_type}: {error}"

# ===== install_mods/install_registry.py (logs) =====
LOG_REPLACE_EXISTING = "[UPDATE INSTALL] Archivo de mod existente reemplazado: {old_file} -> {new_file}"
LOG_REPLACE_REMOVE_FAILED = "[WARN] No se pudo eliminar el archivo de mod reemplazado '{old_file}': {error}"
LOG_REPLACE_DISABLED_REMOVE_FAILED = "[WARN] No se pudo eliminar el archivo de mod desactivado reemplazado '{old_file}': {error}"
LOG_JSON_UPDATING = "[JSON WRITE] Actualizando entrada existente en lista de mods:\n   ↳'{mod_name}'"
LOG_REPLACE_OPTIONS_FOUND = "[REPLACE] '{mod_name}': se encontraron {count} opcion(es) de archivo existente."
LOG_INSTALLED = "[INSTALLED] '{mod_name}'"
LOG_INSTALLED_KEPT_EXISTING = "[INSTALLED] '{mod_name}': se conservaron archivo(s) existente(s) y se instalo archivo nuevo."
LOG_JSON_WRITE_COMPLETE = (
    "[JSON WRITE COMPLETE] profile_mods_list.json se actualizo correctamente.\n"
    "[SUMMARY] Actualizados: {updated_count}, Nuevos: {new_count}, Total: {total_count}."
)
LOG_JSON_WRITE_ERROR = "[ERROR] No se pudo actualizar la lista de mods: {error}"

# ===== install_mods/install_utilities.py (logs) =====
LOG_STAGING_ERROR = "[STAGING ERROR] No se pudo preparar {file_name}: {error}"
LOG_STAGED = "[STAGED] Se prepararon {count} mod(s) en:\n -> {staged_list}\n[SOURCE] -> {mods_source}"
LOG_REPLACEMENT_TIMEOUT = "[WARN] Tiempo agotado esperando la ventana de confirmacion de reemplazo."

# ===== install_mods/archive_handler/progress.py (logs) =====
LOG_PROGRESS = "[{stage_key}] {label} [{percent}%]"
LOG_EXTRACTING = "[EXTRACTING] {label} [0%]"
LOG_INSTALLING_PROGRESS = "[INSTALLING] {label} [0%]"

# ===== nexus/updates.py (logs) =====
LOG_UPDATE_SCAN_START = "[UPDATE SCAN] Perfil Actual: {profile_name} | Comprobando actualizaciones disponibles...\n"
LOG_UPDATE_SCAN_MOD = "→ Mod: {file_name} | Local: {local_version} | Ultima: {latest_version} | "
LOG_UPDATE_SCAN_COMPLETED = " \n[UPDATE SCAN COMPLETED] {scan_label} | actualizaciones encontradas: {updated_count}"
LOG_UPDATE_SCAN_COMPLETED_ALT = "\n[UPDATE SCAN COMPLETED] {scan_label} | actualizaciones encontradas: {updated_count}"

# ===== nexus/nexus_sync.py (logs) =====
LOG_NEXUS_MODS_DIR_MISSING = "[NEXUS] Falta mods_dir, usando respaldo: {fallback_dir}"
LOG_NEXUS_MODS_DIR_ERROR = "[NEXUS][ERROR] mods_dir invalido. Proporcionado: {mods_dir} | Respaldo: {fallback_dir} | Perfil: {profile_name}"
LOG_NEXUS_SAVING = "[NEXUS][SAVE] Guardando datos de mod recopilados en {tracked_file}"
LOG_NEXUS_INFO_UPDATED_LOG = "[NEXUS] informacion actualizada para {updated_count} mod(s)."

# ===== nexus/downloads.py (logs) =====
LOG_NEXUS_REDIRECT_STANDARD = "[NEXUS - STANDARD] Redirigiendo a pagina de archivos del mod para descargar: {target_url}"
LOG_NEXUS_OPEN_FAILED = "[NEXUS] Error al abrir pagina de archivos del mod: {error}"
LOG_DOWNLOADING = "[DOWNLOADING] {out_path}"
LOG_DOWNLOAD_FAILED = "[DOWNLOAD] Error para '{display_label}': {error}"
LOG_DOWNLOAD_COMPLETED = "[DOWNLOAD] Completado: {downloaded} archivo(s) descargado(s)."

# ===== nexus/browse_mods/browser_window.py (logs) =====
LOG_BROWSER_CLOSED = "[NEXUS_BROWSER] Cerrado"
LOG_BROWSER_NO_GAME = "[NEXUS_BROWSER] No hay game_var disponible"

# ===== nexus/protocol_handler/nxm/nxm_actions.py (logs) =====
LOG_NXM_RECEIVED = "[NXM] URL recibida: {nxm_url}"
LOG_NXM_PARSE_FAILED = "[NXM][ERROR] No se pudo interpretar URL NXM: {nxm_url}"
LOG_NXM_GAME_MISMATCH_LOG = "[NXM] Juego no coincide: NXM={game_slug}, perfil activo={profile_game_slug}"
LOG_NXM_DOWNLOAD_EVENT = (
    "[NXM] Evento de descarga de Nexus recibido: Juego: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[NXM] CZT instalara automaticamente tu archivo cuando termine la descarga.\n"
    "[NXM] Espera por favor..."
)
LOG_NXM_DOWNLOAD_FAILED = "[NXM] La descarga fallo o fue cancelada"
LOG_NXM_DOWNLOAD_COMPLETE = "[NXM] Descarga completa: {result}"

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py (logs) =====
LOG_CZTMM_RECEIVED = "[CZTMM] URL recibida: {cztmm_url}"
LOG_CZTMM_PARSE_FAILED = "[CZTMM][ERROR] No se pudo interpretar URL: {cztmm_url}"
LOG_CZTMM_GAME_MISMATCH_LOG = "[CZTMM] Juego no coincide: CZTMM={game_slug}, perfil actual={profile_game_slug}"
LOG_CZTMM_DOWNLOAD_EVENT = (
    "[CZTMM] Evento de descarga de Nexus recibido: Juego: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[CZTMM] CZT instalara automaticamente tu archivo cuando termine la descarga.\n"
    "[CZTMM] Espera por favor..."
)
LOG_CZTMM_DOWNLOAD_EVENT_STANDARD = (
    "[CZTMM] Evento de descarga de Nexus recibido: Juego: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[CZTMM] [CUENTA NEXUS STANDARD DETECTADA] \n"
    "[CZTMM] ¡No olvides presionar 'Slow Download' en tu navegador!\n"
    "[CZTMM] CZT instalara automaticamente tu archivo cuando termine la descarga.\n"
    "[CZTMM] Espera por favor...\n"
)

# ===== nexus/account_type_status.py (logs) =====
LOG_NEXUS_ACCOUNT_TIER_FAILED = "[CZTMM] No se pudo resolver el nivel de cuenta de Nexus, usando standard por defecto: {error}"

# ===== nexus/manual_download_install.py (logs) =====
LOG_NO_DOWNLOAD_DETECTED = "[CZTMM] No se detecto una descarga completada recientemente; auto-instalacion omitida."
LOG_INSTALLING_DOWNLOAD = "[CZTMM] Instalando archivo descargado: {chosen_path}"

# ===== nexus/browse_mods/browser_ext.py (logs) =====
LOG_BROWSER_JS_WITH_SOURCE = "[NEXUS_BROWSER][JS] {text} ({source}:{line_number})"
LOG_BROWSER_JS = "[NEXUS_BROWSER][JS] {text}"

# ===== nexus/browse_mods/marquee_label.py =====
BANNER_TEXT_FREE = (
    "Cuenta Nexus standard detectada — "
    "Esta funcion esta disenada para cuentas premium — "
    "Nexus restringe las descargas directas desde apps remotas para cuentas gratuitas — "
    "Nexus aplica las mismas limitaciones en Vortex."
)
BANNER_TEXT_PREMIUM = (
    "No necesitas iniciar sesion para explorar o descargar mods, para eso sirve la clave API en el menu de setup "
    "— Para usar este navegador, ve a un mod de tu eleccion y luego haz clic en el boton 'Download + Install Current Mod' "
    "— La informacion del mod se guarda en tu archivo local de lista de mods en el momento de la descarga"
)
LOG_ACCOUNT_TIER_FALLBACK = "[NEXUS_BROWSER] No se pudo resolver el nivel de cuenta, usando gratis por defecto: {error}"

# ===== nexus/protocol_handler/nxm/nxm_runtime.py (logs) =====
LOG_NXM_STARTUP_REG_FAILED = "[NXM] Error al aplicar ajuste de registro de inicio: {error}"
LOG_NXM_SENT_URL = "[NXM] URL enviada a instancia en ejecucion: {protocol_url_arg}"
LOG_NXM_SEND_FAILED = "[NXM] Error al enviar URL a instancia en ejecucion: {error}"
LOG_NXM_IPC_FAILED = "[NXM][ERROR] Error al iniciar servidor IPC de NXM"

# ===== working/multi_download_progress_dialog.py & download_progress_session.py =====
DLG_TITLE_DOWNLOADING_MODS    = "Descargando mods"
DLG_TITLE_DOWNLOADING_UPDATES = "Descargando actualizaciones de mods"
LBL_DOWNLOAD_ROW_DEFAULT      = "Descarga #{num}"
LBL_DOWNLOADS_COMPLETE        = "{done} / {total} descargas completadas"
LBL_DOWNLOADS_REMAINING       = "{count} restantes en la cola"

# ===== install_mods/consolidated_install_dialog.py & flujo de fijado de loadout =====
DLG_TITLE_RESOLVE_INSTALL     = "Resolver opciones de instalacion"
DLG_TITLE_SELECT_FILES_PIN    = "Selecciona archivos para fijar"
LBL_RESOLVE_HEADER            = "{count} mod(s) requieren atencion.\nHaz tus selecciones y pulsa Aplicar."
LBL_HDR_MOD_ARCHIVE           = "Archivo del Mod:"
LBL_HDR_INSTALLED_MOD         = "Mod Instalado:"
LBL_HDR_CHOOSE_DOWNLOAD       = "Elige un archivo para descargar:"
LBL_HDR_SELECT_LOADOUT_FILE   = "Selecciona el archivo para el loadout:"
LBL_HDR_ARCHIVE_OPTIONS       = "Opciones del Archivo: (selecciona un archivo a instalar)"
LBL_HDR_REPLACE_OR_NEW        = "Reemplazar un archivo existente o instalar como nuevo:"
LBL_UNKNOWN_MOD               = "(desconocido)"
LBL_FILE_NUM                  = "Archivo {file_id}"
OPT_SKIP_DOWNLOAD             = "(omitir descarga)"
OPT_INSTALL_NEW               = "(instalar como nuevo)"
OPT_INSTALL_ALL               = "Instalar Todo"
OPT_SKIP                      = "Omitir"
MSG_BROKEN_LINK               = "(enlace roto — descargar manualmente)"
MSG_BROKEN_LINK_URL           = "(enlace roto — ver {url})"
BTN_APPLY                     = "Aplicar"
BTN_SKIP_ALL                  = "Omitir Todo"
BTN_USE_THIS_FILE             = "Usar Este Archivo"
BTN_SELECT_FILE               = "Seleccionar Archivo"
LBL_PIN_SELECT_HEADER         = "Selecciona archivo para fijar"
LBL_CTX_MOD_NAME              = "Nombre del Mod: {name}"
LBL_CTX_LOADOUT               = "Loadout: {name}"
LBL_CTX_INSTALLED_FILE        = "Archivo Instalado: {name}"
LBL_CTX_MOD_FILE              = "Archivo del Mod: {name}"
LBL_MOD_FALLBACK              = "Mod {mod_id}"
LBL_TARGET_UNKNOWN            = "desconocido"


# ===== nexus/protocol_handler/nxm/nxm_register.py (logs) =====
LOG_NXM_REGISTERED = "[NXM] Manejador de protocolo nxm:// registrado: {command}"
LOG_NXM_REGISTER_FAILED = "[NXM][ERROR] Error al registrar manejador nxm://: {error}"
LOG_NXM_UNREGISTERED = "[NXM] Manejador de protocolo nxm:// desregistrado"
LOG_NXM_UNREGISTER_FAILED = "[NXM][ERROR] Error al desregistrar manejador nxm://: {error}"

# ===== nexus/protocol_handler/cztmm/cztmm_register.py (logs) =====
LOG_CZTMM_REGISTERED = "[CZTMM] Manejador de protocolo cztmm:// registrado: {command}"
LOG_CZTMM_REGISTER_FAILED = "[CZTMM][ERROR] Error al registrar manejador cztmm://: {error}"
LOG_CZTMM_UNREGISTERED = "[CZTMM] Manejador de protocolo cztmm:// desregistrado"
LOG_CZTMM_UNREGISTER_FAILED = "[CZTMM][ERROR] Error al desregistrar manejador cztmm://: {error}"

# ===== loadout_system/ls_ui_manage_dialog.py (logs) =====
LOG_LOADOUT_ROOT_NOT_SET = "[LOADOUT] Carpeta raiz no configurada. No se pueden gestionar loadouts."

# ===== loadout_system/download_list.py (logs) =====
LOG_LOADOUT_SAVE_FAILED_DL = "[LOADOUT] Error al guardar loadouts importados desde Download Mod List."
LOG_LOADOUT_IMPORTED_DL = "[LOADOUT] Se importaron {added_count} loadout(s) a los loadouts guardados del perfil '{profile_name}' desde Download Mod List."
LOG_DOWNLOAD_CANCELED = "[LOADOUT DOWNLOAD] Download Mod List cancelado en el mensaje de confirmacion de redescarga."
LOG_DOWNLOAD_SUMMARY = "[SUMMARY] Descargados: {downloaded} | Omitidos por existentes: {skipped} | Fallidos: {failed}"
LOG_DOWNLOAD_INSTALL_QUEUED = "[INSTALL] Otra instalacion interna por descarga esta en ejecucion. Encolando esta solicitud de instalacion."
LOG_DOWNLOAD_INSTALL_FAILED = "[INSTALL] Fallo del worker de descarga-instalacion: {error}\n{traceback}"
LOG_LOADOUT_AUTO_SELECT_FAILED = "[LOADOUT] No se pudo auto-seleccionar el loadout importado '{loadout_name}': {error}"

# ===== loadout_system/importing.py (logs) =====
LOG_LOADOUT_IMPORTED = (
    "[LOADOUT] Se importaron {added_count} loadout(s) desde '{imported_path}'. \n"
    "Entradas agregadas a la lista principal de mods: {profile_metadata_added}. \n"
    "Entradas actualizadas en la lista principal de mods: {profile_metadata_updated}."
)

# ===== loadout_system/build_loadout.py (logs) =====
LOG_LOADOUT_MERGE_FAILED = "[LOADOUT] Error al guardar loadouts combinados para el perfil '{profile_name}': {error}"

# ===== loadout_system/apply_loadout.py (logs) =====
LOG_LOADOUT_ROOT_NOT_SET_APPLY = "[LOADOUT] Carpeta raiz no configurada. No se puede aplicar loadout."
LOG_LOADOUT_NO_MODS = "[LOADOUT] No se encontraron mods para el loadout '{loadout_name}'."
LOG_LOADOUT_ROOT_NOT_SET_APPLY_MULTI = "[LOADOUT] Carpeta raiz no configurada. No se pueden aplicar loadouts."
LOG_LOADOUT_NO_MODS_MULTI = "[LOADOUT] No se encontraron mods para los loadouts seleccionados."

# ===== loadout_system/storage.py (logs) =====
LOG_LOADOUT_REMOVE_FAILED = "[LOADOUT] Error al eliminar archivos de loadout existentes: {error}"
LOG_LOADOUT_SAVE_FAILED = "[LOADOUT] Error al guardar loadouts: {error}"

# ===== loadout_system/select_file_variant.py (logs) =====
LOG_FILE_PIN_SKIPPED = "[LOADOUT] Fijado de archivo omitido para '{display_name}' ({cache_key}): {error}"

# ===== loadout_system/ls_utilities.py (logs) =====
LOG_FILE_CANDIDATES_FAILED = "[LOADOUT] Error al cargar candidatos de archivo para {loadout_name}:{mod_id}: {error}"
LOG_FILE_PIN_SELECTION_SKIPPED = "[LOADOUT] Seleccion de fijado de archivo omitida para {loadout_name}:{mod_id}: {error}"

# ===== Get_SteamLibraries.py (logs) =====
LOG_STEAM_SCAN_DRIVE = "[STEAMLIB][SCAN] Escaneando unidad {drive_root} para libraryfolders.vdf (UPDATED)"
LOG_STEAM_SCAN_LEGACY = "[STEAMLIB][SCAN] Escaneando unidad {drive_root} para libraryfolder.vdf (LEGACY)"
LOG_STEAM_SEARCHING = "[STEAMLIB][SCAN] Buscando... {pattern}"
LOG_STEAM_LOCATED = "[STEAMLIB] [LOCATED] libraryfolders.vdf @ {vdf} (UPDATED)"
LOG_STEAM_LOCATED_LEGACY = "\n[STEAMLIB] [LOCATED] libraryfolder.vdf @ {vdf} (LEGACY)"
LOG_VDF_PARSING = "[VDF] Interpretando archivo VDF..."
LOG_STEAM_ADDED = "[STEAMLIB][ADDED] ↾ {lib_common}"
LOG_STEAM_PARSE_WARN = "[WARN] No se pudieron interpretar las bibliotecas de Steam: {error}"
LOG_STEAM_SKIP_SCAN = "[STEAMLIB] Omitiendo escaneo de biblioteca Steam: el modo de ruta para '{current_profile}' es '{pathing_mode}'."
LOG_STEAM_RUN_UTIL = "[RUN UTIL] ▶ SteamLibrarySearchUtility ◀"
LOG_STEAM_SCANNING = "[STEAMLIB] Escaneando bibliotecas de Steam..."
LOG_STEAM_SCAN_SUCCESS = "[STEAMLIB] [SCAN SUCCESSFUL]\n    ↾ Todas las rutas de bibliotecas de Steam actualizadas."
LOG_STEAM_WARN_NO_ROOT = "⚠️ [WARNING] No se puede guardar la configuracion porque czt_root_folder no existe."
LOG_EXE_DETECTED = "[EXE DETECTED] Encontrado @ {path}"
LOG_EXE_NOT_FOUND = "[EXE DETECT] No se encontro un exe valido."
