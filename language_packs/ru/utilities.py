# Utilities Global - Русские строки

# ===== basic_global_utilities.py =====
LOG_WARN_NO_ROOT_SAVE = "⚠️ [WARNING] Невозможно сохранить конфиг, потому что czt_root_folder не существует."
LOG_UNRAR_NOT_FOUND = "[UNRAR] Рабочий инструмент UnRAR не найден. Задайте 'unrar_path' в настройках или установите WinRAR (UnRAR.exe)."
DLG_TITLE_SELECT_DRIVE = "Выбор диска"
LBL_SELECT_DRIVE = "Выберите диск для папок Mod Manager:"
BTN_OK = "Ок"
BTN_CANCEL = "Отмена"

# ===== CheckForCZTUpdates.py =====
WELCOME_MESSAGE = (
    "🔄️ Автоустановка модов:\n"
    "- Скачивайте моды с сайта nexus. (используйте кнопку 'Mod Manager Download')\n"
    "- Это запустит CZT, и приложение автоматически выполнит установку + сохранение информации о моде.\n"
    "- Если кнопки 'Mod Manger Download' нет, скачайте расширение CZT с github.\n"
    "- Расширение CZT позволяет кнопке ручной загрузки работать как 'Mod Manager Download'.\n\n"
    "🛠️ Ручная установка модов:\n"
    "- Перетащите файлы модов в это окно лога, чтобы подготовить их к установке.\n"
    "- Выберите моды в списке и нажмите ➡️ (вверху справа), чтобы продолжить.\n\n"
    "💡 [HINT]\n"
    "- У большинства элементов UI есть подсказки, наведите курсор на кнопки и другие элементы. \n"
    "- Нажмите SHIFT + H, чтобы показать доступные горячие клавиши.\n"
    "- Нажмите F2, чтобы открыть меню порядка загрузки.\n"
)
DLG_TITLE_BETA_AVAILABLE = "Доступна бета"
DLG_TITLE_UPDATE_AVAILABLE = "Доступно обновление"
LBL_BETA_AVAILABLE = "Доступна новая бета-версия CZT!"
LBL_UPDATE_AVAILABLE = "Доступна новая версия CZT Mod Manager!"
LBL_VERSION_INFO = "Текущая: {local_version}\nПоследняя: {latest_version}"
BTN_DOWNLOAD_INSTALL = "Скачать и установить ({tag})"
BTN_DISMISS = "Закрыть"
BTN_IGNORE = "Игнорировать"
BTN_CLOSE = "Закрыть"
BTN_CHECK_FOR_UPDATES = "Проверить обновления"
MSG_HOTKEY_CONTROLS = (
    "\n\n"
    "[ГОРЯЧИЕ КЛАВИШИ]\n"
    "    > F2           : Открыть меню порядка загрузки.\n"
    "    > F3           : Открыть меню плагинов.\n"
    "    > F5           : Центрировать главное окно на экране.\n"
    "    > F9           : Определить отсутствующие моды из сохранённого лоадаута.\n"
    "    > CTRL+O       : Открыть корневую папку CZT.\n"
    "    > Shift+H      : Показать список горячих клавиш.\n"
    "    > Shift+C      : Показать текущую конфигурацию.\n"
    "    > Shift+R      : Показать пути к файлам ресурсов.\n"
    "    > Ctrl+Shift+L : Запустить игру.\n"
    "    > Ctrl+Shift+S : Открыть консоль отладки.\n        \n"
)
DLG_TITLE_PATCH_NOTES = "История изменений"
LBL_PATCH_NOTES = "CZT Mod Manager — История изменений"
DLG_TITLE_UPDATE_ERROR = "Ошибка обновления"
MSG_UPDATE_ERROR = "Не удалось скачать или запустить установщик:\n{error}"
MSG_NO_RELEASE_NOTES = "Для этого канала обновлений не найдено заметок к релизу."
MSG_RELEASE_NOTES_ERROR = "Не удалось получить заметки к релизу: {error}"

# ===== load_order.py =====
DLG_TITLE_LOAD_ORDER = "Порядок загрузки"
MSG_LOAD_ORDER_NO_PROFILE = "Не удалось определить текущий профиль."
MSG_LOAD_ORDER_NO_PROFILE_SET = "Текущий профиль не задан."
MSG_LOAD_ORDER_PROFILE_NOT_FOUND = "Конфиг профиля не найден: {profile_name}"
MSG_LOAD_ORDER_MODS_DIR_MISSING = "Папка модов для профиля не существует: {profile_name}"
DLG_TITLE_SET_LOAD_ORDER = "Задать порядок загрузки - {profile_name}"
DLG_TITLE_LOAD_ORDER_BLOCKED = "Порядок загрузки недоступен"
MSG_LOAD_ORDER_BLOCKED_PROFILE = "Меню порядка загрузки отключено для этого профиля: {profile_name}"
LBL_LOAD_ORDER_TITLE = "Выберите мод и используйте элементы ниже, чтобы создать файл порядка загрузки."
LBL_LOAD_ORDER_SUBTITLE = "> Нажмите 'Сохранить порядок', чтобы применить изменения, затем запустите игру.\n> Порядок загрузки сохраняется, пока вы его не измените."
BTN_LOAD_ORDER_MOVE_UP = "Вверх"
BTN_LOAD_ORDER_MOVE_DOWN = "Вниз"
BTN_LOAD_ORDER_SAVE_ORDER = "Сохранить порядок"
LBL_LOAD_ORDER_LEGEND_CONTROLS = "Управление:"
LBL_LOAD_ORDER_LEGEND_MOVE_UP = "Вверх"
LBL_LOAD_ORDER_LEGEND_MOVE_DOWN = "Вниз"
LBL_LOAD_ORDER_LEGEND_DRAG = "Перетаскивание: переместить вверх или вниз"
LBL_LOAD_ORDER_LEGEND_SAVE = "Сохранить: задать порядок загрузки"
DLG_TITLE_SAVE = "Сохранить"
MSG_LOAD_ORDER_SAVED = "Порядок загрузки успешно сохранен."
DLG_TITLE_ERROR_SAVING = "Ошибка сохранения"
MSG_LOAD_ORDER_SAVE_FAILED = "Не удалось сохранить порядок загрузки:\n{error}"

# ===== plugins/F3_Menu.py =====
DLG_TITLE_PLUGIN_MANAGER = "Менеджер плагинов"
BTN_PLUGIN_MENU = "Меню плагинов"
LBL_PLUGIN_MANAGER_INSTALLED = "Установленные плагины"
BTN_PLUGIN_MANAGER_RESCAN = "Пересканировать"
MSG_PLUGIN_MANAGER_NOT_INITIALISED = "Менеджер плагинов не инициализирован."
MSG_PLUGIN_MANAGER_EMPTY = (
    "Плагины не найдены.\n\n"
    "Поместите папки плагинов в:\n  {plugins_root}\n\n"
    "Каждая папка плагина должна содержать manifest plugin.json."
)
CB_PLUGIN_ENABLE_PROFILE_FMT = "Профиль ({profile})"
LBL_PLUGIN_PROFILE_NONE = "нет"
BTN_PLUGIN_OPEN_FOLDER = "Открыть папку"
MSG_PLUGIN_MANAGER_SAVE_FAILED = "Не удалось сохранить конфиг:\n{error}"
MSG_PLUGIN_ROOT_NOT_SET = "Корневая папка CZT не задана. Невозможно загрузить плагины."
LBL_PLUGIN_STANDALONE_EXE = "Отдельные EXE:"
LBL_PLUGIN_SCRIPTS = "Скрипты:"
LBL_PLUGIN_NONE_STANDALONE = "Отдельные EXE-плагины не найдены."
LBL_PLUGIN_NONE_SCRIPTS = "Скриптовые плагины не найдены."
CB_PLUGIN_ENABLE_PROFILE = "Включить для профиля"
CB_PLUGIN_ENABLE_GLOBAL = "Включить глобально"
CB_PLUGIN_RUN_STARTUP = "Запускать при старте"
BTN_PLUGIN_RUN = "Запустить"
BTN_PLUGIN_UNLOAD = "Выгрузить"
BTN_PLUGIN_SAVE_STARTUP_OPTIONS = "Сохранить параметры запуска"
BTN_PLUGIN_CLOSE = "Закрыть"
DLG_TITLE_PLUGIN_RUN_AS_ADMIN = "Запустить от имени администратора? (необязательно)"
MSG_PLUGIN_RUN_AS_ADMIN = "Запустить {plugin_name} от имени администратора?"
DLG_TITLE_PLUGIN = "Плагин"
MSG_PLUGIN_LAUNCHED = "Запущено: {plugin_name}"
DLG_TITLE_PLUGIN_ERROR = "Ошибка плагина"
MSG_PLUGIN_LAUNCH_FAILED = "Не удалось запустить плагин:\n{error}"
MSG_PLUGIN_UNLOAD_FAILED = "Не удалось выгрузить плагин:\n{error}"
MSG_PLUGIN_UNLOADED = "Выгружено: {plugin_name}\n\nПримечание: это только удаляет модуль из памяти.\nПотоки, сигналы или элементы UI могут остаться, если плагин не очищает себя сам."
MSG_PLUGIN_NOTHING_TO_UNLOAD = "Нечего выгружать для: {plugin_name}"
DLG_TITLE_PLUGIN_STARTUP_REQUIREMENTS = "Требования запуска не выполнены"
MSG_PLUGIN_STARTUP_REQUIREMENTS = "Плагины для автозапуска должны быть включены глобально или для профиля.\nЭти плагины не будут загружены при старте, пока вы это не исправите:\n- {plugins}"
DLG_TITLE_SAVED = "Сохранено"
MSG_PLUGIN_OPTIONS_SAVED = "Параметры плагинов сохранены."
DLG_TITLE_SAVE_ERROR = "Ошибка сохранения"
MSG_PLUGIN_OPTIONS_SAVE_FAILED = "Не удалось сохранить параметры плагинов:\n{error}"

# ===== popup_policies.py =====
POPUP_TITLE_CUSTOM_SETTINGS = "Пользовательские настройки"
POPUP_TITLE_MANAGE_LOADOUTS = "Управление лоадаутами"
POPUP_TITLE_FIRST_TIME_SETUP = "Первоначальная настройка"
POPUP_TITLE_RESTORE_BACKUP = "Восстановление из резервной копии"
POPUP_TITLE_FORCE_UPDATE_OPTIONS = "Параметры принудительного обновления"
POPUP_TITLE_CLEAN_OPTIONS = "Параметры очистки"

# ===== UserSetup_Actions.py =====
DLG_TITLE_NO_DRIVES = "Нет дисков"
MSG_NO_DRIVES = "Доступные диски не найдены."
DLG_TITLE_NO_ROOT_FOLDER = "Нет корневой папки"
MSG_NO_ROOT_FOLDER = "Корневая папка CZT не задана или не существует."
DLG_TITLE_ROOT_CREATED = "Корень создан"
MSG_ROOT_CREATED = "Корневые папки CZT созданы в: {czt_root_folder}"
DLG_TITLE_SELECT_UNRAR = "Выберите исполняемый файл UnRAR"
MSG_UNRAR_INSTALLER_PROMPT = (
    "Далее запустится установщик UnRAR.\n"
    "Установите в папку:\n"
    " > Drive_Selected_For_Root\\CZT Mod Manager\\czt_tools <"
)
LOG_UNRAR_INSTALLER_LAUNCHED = (
    "Установщик UnRAR запущен. Пожалуйста, завершите установку.\n"
    " Установка считается завершенной после процесса извлечения!"
)

# ===== backups/mod_backup.py =====
DLG_TITLE_CREATE_BACKUP = "Создать резервную копию"
MSG_BACKUP_ROOT_NOT_SET = "Корневая папка не настроена."
MSG_BACKUP_CHOOSE = "Выберите, что резервировать:"
BTN_BACKUP_MOD_FILES = "Только файлы модов"
BTN_BACKUP_MODS_LIST = "Только mods_list.json"
BTN_BACKUP_FILES_AND_LIST = "Резервировать файлы + список"
MSG_BACKUP_SUCCESS = "Резервная копия успешно создана.\n\n"
MSG_BACKUP_WARNINGS = "Резервное копирование завершено с предупреждениями.\n\n"
MSG_BACKUP_FAILED = "Сбой резервного копирования.\n\n"

# ===== backups/restore_backup.py =====
DLG_TITLE_RESTORE_BACKUP = "Восстановление из резервной копии"
MSG_RESTORE_ROOT_NOT_SET = "Корневая папка не настроена."
MSG_RESTORE_BACKUPS_NOT_FOUND = "Папка резервных копий не найдена: {backup_root}"
LBL_RESTORE_HEADER = "Выберите папки резервных копий для восстановления или удаления"
LBL_NO_BACKUPS = "Резервные копии не найдены"
LBL_BACKUP_META = "Содержит: {kind_text}   |   Создано: {stamp}"
MSG_RESTORE_SELECT_ONE = "Выберите одну резервную копию для установки."
MSG_RESTORE_ONLY_ONE = "Установка поддерживает ровно одну выбранную резервную копию за раз."
MSG_RESTORE_SELECT_DELETE = "Выберите одну или несколько резервных копий для удаления."
MSG_DELETE_SINGLE = "Удалить резервную копию '{name}'?"
MSG_DELETE_MULTIPLE = "Удалить {count} папок резервных копий?\n\n{preview}{extra}"
DLG_TITLE_DELETE_BACKUP = "Удалить резервную копию"
MSG_DELETE_ERRORS = "Некоторые папки резервных копий не удалось удалить:\n\n"
BTN_INSTALL_SELECTED = "Установить выбранное"
BTN_DELETE_SELECTED = "Удалить выбранное"
MSG_RESTORE_CONFIRM = "Восстановить резервную копию '{backup_name}' для профиля '{profile_name}'?"
MSG_RESTORE_CONFIRM_DETAIL = "Это заменит текущие включенные/отключенные файлы модов, сохраненные лоадауты и/или profile_mods_list.json."
MSG_RESTORE_SUCCESS = "Восстановление успешно завершено.\n\n"
MSG_RESTORE_WARNINGS = "Восстановление завершено с предупреждениями.\n\n"
MSG_RESTORE_FAILED = "Сбой восстановления.\n\n"

# ===== install_mods/process_install.py =====
DLG_TITLE_NOTHING_SELECTED = "Ничего не выбрано"
MSG_NO_MODS_SELECTED_INSTALL = "Для установки не выбраны моды."
DLG_TITLE_CONFIRM_INSTALL = "Подтвердить установку"
MSG_CONFIRM_INSTALL_LIST = "Установить следующие {count} мод(ов)?\n\n{mod_list}"
MSG_CONFIRM_INSTALL_COUNT = "Установить выбранные {count} мод(ов)?"
DLG_TITLE_ERROR = "Ошибка"
MSG_NO_ROOT_FOLDER_INSTALL = "Корневая папка не задана! Нажмите setup и создайте корневую папку перед установкой модов."
MSG_SELECTED_MODS_NOT_FOUND = "Выбранные файлы модов не найдены."
DLG_TITLE_CONFIRM_SOURCE_DELETE = "Подтвердить удаление источника"
MSG_CONFIRM_SOURCE_DELETE = "Удалить оставшиеся архивы модов из папки источника после установки?\n\n{preview}{extra}"

# ===== install_mods/process_uninstall.py =====
MSG_NO_FILES_SELECTED_DELETE = "Не выбраны файлы для удаления."
DLG_TITLE_CONFIRM_DELETE = "Подтвердить удаление"
MSG_CONFIRM_DELETE_COUNT = "Вы уверены, что хотите удалить {count} файл(ов)?"

# ===== install_mods/dying_light_auto_patch.py =====
DLG_TITLE_DL_DATA_SLOT = "Заменить слот данных Dying Light"
LBL_DL_DATA_SLOT_CHOOSE = "Выберите существующий файл данных Dying Light для замены перед установкой, установите как новый в следующий свободный слот или отмените установку."
LBL_DL_SOURCE_MOD = "Исходный мод: {source_display}"
LBL_DL_INSTALLING = "Установка: {incoming_file}"
LBL_DL_PROFILE = "Профиль: {profile_name}"
BTN_INSTALL_AS_NEW = "Установить как новый"
BTN_INSTALL_AS_NEW_SLOT = "Установить как новый ({target})"
BTN_CANCEL_INSTALL = "Отменить установку"
LBL_DL_STATE_ACTIVE = "Активен"
LBL_DL_STATE_DISABLED = "Отключен"

# ===== install_mods/archive_handler/archive_handler_core.py =====
DLG_TITLE_ARCHIVE_INSTALL_CHOICE = "Выбор установки архива"
MSG_ARCHIVE_MULTI_CANDIDATES = "В архиве найдено несколько кандидатов для установки:\n{archive_title}\n\nРазрешенные расширения для этого профиля: {exts_label}\nВыберите одного кандидата для установки, установить все или пропустить архив."
BTN_INSTALL_ALL = "Установить все"
BTN_SKIP_ARCHIVE = "Пропустить этот архив"
DLG_TITLE_SELECTION_REQUIRED = "Требуется выбор"
MSG_SELECT_CANDIDATE_FIRST = "Сначала выберите кандидата или используйте 'Установить все'."
DLG_TITLE_ARCHIVE_FOLDER_CHOICE = "Выбор папки архива"
MSG_ARCHIVE_MULTI_FOLDERS = "В архиве найдено несколько папок-кандидатов для установки:\n{archive_title}\n\nВыберите папку-кандидат для установки, установить все или пропустить архив."

# ===== install_mods/replacement_handler/resolve_replacement.py =====
DLG_TITLE_SELECT_REPLACEMENT = "Выбор цели замены"
MSG_REPLACEMENT_DEFAULT = "Найдены совпадающие/похожие файлы. Выберите, какой файл заменить, или пропустите замену."
BTN_SKIP_REPLACEMENT = "Пропустить замену (установить новый файл/заменить точное совпадение)"

# ===== launch_game/launcher_core.py =====
MSG_NO_INSTALL_DIR = (
    "Не задана корректная папка установки!\n \n- Режим путей [STEAM]:\n   > Нажмите 'Detect Steam'\n "
    "\n- Режим путей [Manual]:\n   > Нажмите 'SET INSTALL' и 'SET EXE' для настройки."
)
MSG_EXE_NOT_FOUND = "Не удалось найти EXE для {game_name}!\n"
DLG_TITLE_CZT_LAUNCHER = "CZT Launcher"
MSG_LAUNCH_OPTIONS = (
    "Параметры запуска {game_name}: \n\n"
    " ➡️ Link | Modded = Подключить включенные моды.\n"
    " ➡️ Unlink | Safe = Удалить существующие ссылки.\n"
    " ➡️ Cancel = Отменить запуск ракеты!"
)
BTN_LINK_MODDED = "Link | Modded"
BTN_UNLINK_SAFE = "Unlink | Safe"
MSG_ELEVATION_REQUIRED = "Требуются повышенные права. Попытка перезапуска от администратора.\n\nОшибка: {error}"
MSG_PERMISSION_DENIED = "Доступ запрещен.\n\nОшибка: {error}"
MSG_LAUNCH_TOGGLE_FAILED = "Не удалось переключить моды или запустить игру:\n{error}"

# ===== launch_game/launcher_utilities.py =====
MSG_ELEVATION_FAILED = "Не удалось повысить права до администратора: {error}"
MSG_SYMLINK_PERMISSIONS = (
    "Windows требует права администратора для создания симлинков.\n\n"
    "Выберите вариант:\n"
    "- Запустить приложение от имени администратора.\n"
    "- Включить режим разработчика в настройках Windows для постоянного обхода.\n"
    "    ↳ Права администратора не нужны!\n"
)
BTN_RUN_AS_ADMIN = "Запустить от имени администратора"
BTN_OPEN_WIN_SETTINGS = "Открыть настройки Windows"
MSG_DEV_MODE_OPEN_FAILED = "Не удалось открыть настройки режима разработчика."

# ===== launch_game/log_messages.py =====
LOG_AUDIO_MENU_MUSIC_PAUSED = "[AUDIO] Музыка меню приостановлена. Перезапустите CZT для сброса или пересохраните аудио-настройки для возобновления."
LOG_LAUNCH_LOAD_ORDER_READ_FAILED = "[LAUNCH] Не удалось прочитать порядок загрузки: {error}"
LOG_CONFIG_RELOAD_FAILED = "[ERROR] Не удалось перезагрузить конфиг с диска: {error}"
LOG_LAUNCH_SEARCHING_EXE = "[FIRST TIME LAUNCH]\n- Поиск EXE в: {steam_libraries}"
LOG_LAUNCH_EXE_NOT_FOUND = "[ERROR] Не удалось найти EXE для {game_name}!"
LOG_NO_ROOT_SET = "[ERROR] Корневая папка не задана! Нажмите 'CREATE ROOT', чтобы начать использовать CZT."
LOG_LAUNCH_CREATED_MODS_FOLDER = "[LAUNCH] Создана отсутствующая папка модов: {path}"
LOG_LAUNCH_CREATED_MODS_FOLDER_PARENT = "[LAUNCH] Создана родительская папка модов: {path}"
LOG_MODS_FOLDER_PREP_FAILED = "[ERROR] Не удалось подготовить путь папки модов {path}: {error}"
LOG_LAUNCH_CANCELLED = "[LAUNCH] Запуск {game_name} отменен пользователем!"
LOG_TOTAL_LINKED = "[TOTAL] Подключено модов: {count}"
LOG_PER_FILE_REMOVE_FAILED = "[PER-FILE] Не удалось удалить симлинк {path}: {error}"
LOG_TYPE_SYMLINKS_REMOVED = "[{mod_type}] Удалено симлинков: {count}"
LOG_PER_FOLDER_REMOVE_FAILED = "[PER-FOLDER] Не удалось удалить симлинк/джанкшен {path}: {error}"
LOG_PER_FOLDER_REMOVED_COUNT = "[PER-FOLDER] Удалено симлинков/джанкшенов: {count}"
LOG_LINK_DISABLED_MODS_JUNCTION = "[LINK] Джанкшен Mods отключен: {path}"
LOG_LINK_DISABLED_MODS_SYMLINK = "[LINK] Симлинк Mods отключен: {path}"
LOG_LINK_REMOVE_MODS_SYMLINK_FAILED = "[LINK] Не удалось удалить симлинк Mods: {error}"
LOG_LAUNCH_STEAM_START = "[LAUNCH] Steam запускает app ID: {steam_appid} > {game_name} > {mode}"
LOG_STEAM_LAUNCH_FAILED_FALLBACK = "[ERROR] Не удалось запустить через Steam: {error}\nПереход к запуску через EXE."
LOG_LAUNCH_STARTED_GAME = "[LAUNCH] Игра запущена: {exe_path} {mode}"
LOG_ELEVATION_REQUIRED_RELAUNCH = "[ERROR] Требуются повышенные права: {error}\nПробуем перезапустить от администратора..."
LOG_PERMISSION_DENIED_SIMPLE = "[ERROR] Доступ запрещен: {error}"
LOG_LAUNCH_TOGGLE_FAILED_SIMPLE = "[ERROR] Не удалось переключить моды или запустить игру: {error}"
LOG_TYPE_LINKING_TO = "[{mod_type}] Подключение {count} мод(ов) к {destination}"
LOG_MOD_LIST_ITEM = "  - {mod_name}"
LOG_LINK_MODS_DIR_MISSING = "[LINK] Папка модов не найдена или отключена: {path}"
LOG_LINK_EXE_FAILED = "[LINK] Не удалось подключить {file_name} в папку exe: {error}"
LOG_LINK_MODS_FOLDER_NOT_EMPTY = "[LINK] Нельзя заменить существующую папку модов, потому что она не пуста: {path}"
LOG_LINK_PREP_MODS_FOLDER_FAILED = "[LINK] Не удалось подготовить папку Mods для джанкшена: {error}"
LOG_LINK_ENABLED_MODS_SUMMARY = "[LINK] Моды подключены: \n - Источник: {source}\n - Подключено к -> {destination}"
LOG_PER_FILE_CLEAN_FAILED = "[PER-FILE] Ошибка очистки {path}: {error}"
LOG_PER_FILE_LINK_FAILED = "[PER-FILE] Ошибка подключения {file_name}: {error}"
LOG_CONTENT_GAME_DIR_NOT_FOUND = "[CONTENT MOD] Папка Content игры не найдена: {path}"
LOG_CONTENT_BACKUP_FAILED = "{tag} Не удалось сделать резервную копию {path}, пропуск: {error}"
LOG_CONTENT_LINK_FAILED = "{tag} Не удалось подключить {file_name}: {error}"
LOG_CONTENT_SKIP_JUNCTION_REAL_DIR = "{tag} Пропуск джанкшена, реальная папка существует: {sub_name}"
LOG_CONTENT_JUNCTION_FAILED = "{tag} Не удалось создать джанкшен {sub_name}: {error}"
LOG_PER_FOLDER_CLEAN_FAILED = "[PER-FOLDER] Ошибка очистки {path}: {error}"
LOG_PER_FOLDER_LINKED_COUNT = "[PER-FOLDER] Подключено папок: {count} -> {destination}"
LOG_IS_JUNCTION_FAILED = "[ERROR] is_junction завершился ошибкой: {error}"
LOG_RMDIR_FAILED = "[ERROR] rmdir не выполнен для {link}: {error}"
LOG_REMOVE_FILE_LINK_FAILED = "[ERROR] Не удалось удалить файловую ссылку: {link} - {error}"
LOG_REMOVE_JUNCTION_EXCEPTION = "[ERROR] Исключение в remove_junction для {link}: {error}"
LOG_LAUNCH_REFRESHING_SYMLINKS = "[LAUNCH] Обновление симлинков..."
LOG_ASI_DLL_REMOVE_FAILED = "[ASI_DLL] Не удалось удалить asi/dll симлинк {path}: {error}"
LOG_CONTENT_GAME_DIR_NOT_FOUND_SKIP_UNLINK = "[CONTENT MOD] game_content_dir не найден, пропуск unlink: {path}"
LOG_CONTENT_UNLINK_FAILED = "{tag} Не удалось отвязать {path}: {error}"
LOG_CONTENT_RESTORE_FAILED = "{tag} Не удалось восстановить {path}: {error}"
LOG_CONTENT_UNLINKED_COUNT = "{tag} Отвязано модов: {count}"
LOG_CONTENT_ORPHAN_REMOVED = "[CONTENT MOD] Удалено {count} осиротевших ссылок (проверка безопасности)"
LOG_CONTENT_PRESERVE_DIR_CREATED = "[CONTENT MOD] Пересоздана обязательная папка: {path}"
LOG_CONTENT_PRESERVE_DIR_FAILED = "[CONTENT MOD] Не удалось обеспечить обязательную папку {path}: {error}"
LOG_LINK_DISABLED_FOLDER_JUNCTION = "[LINK] Джанкшен папки отключен: {path}"
LOG_LINK_DISABLED_FOLDER_SYMLINK = "[LINK] Симлинк папки отключен: {path}"
LOG_LINK_REMOVE_FOLDER_FAILED = "[LINK] Ошибка удаления ссылки папки {path}: {error}"
LOG_LINK_DISABLED_FILE_SYMLINK = "[LINK] Симлинк файла отключен: {path}"
LOG_LINK_REMOVED_FILE = "[LINK] Файл удален: {path}"
LOG_LINK_REMOVE_FILE_FAILED = "[LINK] Ошибка удаления ссылки файла {path}: {error}"
LOG_ELEVATION_FAILED_SIMPLE = "[ERROR] Ошибка повышения прав: {error}"
LOG_DEV_MODE_SETTINGS_OPEN_FAILED = "[ERROR] Не удалось открыть настройки режима разработчика: {error}"

# ===== install_mods/archive_handler/archive_handler_core.py logs =====
LOG_INSTALL_CONTENT_ADDED_MOD = "[{mod_type}] Добавлен мод: {mod_label}"
LOG_INSTALL_CONTENT_ADDED_FOLDER_MOD = "[{mod_type}] Добавлен папочный мод: {mod_name}"
LOG_COPY_CONTENT_MOD_FOLDER_FAILED = "[ERROR] copy_content_mod_folder завершился ошибкой: {error}"
LOG_INSTALL_FILE_FAILED = "[ERROR] Произошла ошибка при установке {install_name}: {error}"

# ===== loadout_system/detect_missing.py =====
DLG_TITLE_MISSING_MODS = "Отсутствующие моды"
MSG_MISSING_NO_LOADOUTS = "Для профиля '{profile_name}' не найдено сохраненных лоадаутов."
MSG_MISSING_LOADOUT_NOT_FOUND = "Лоадаут '{target_loadout}' не найден."
DLG_TITLE_DETECT_MISSING = "Поиск отсутствующих модов"
LBL_DETECT_MISSING_SELECT = "Выберите лоадаут для сравнения установленных файлов:"
MSG_MISSING_NO_FILES = "В лоадауте '{target_loadout}' нет файлов."
MSG_MISSING_NONE_DETECTED = "Для лоадаута '{target_loadout}' отсутствующие файлы не обнаружены."
MSG_MISSING_FOUND = "Найдено отсутствующих файлов модов для лоадаута '{target_loadout}': {count}."
MSG_MISSING_DOWNLOAD_PROMPT = (
    "Найдено отсутствующих файлов модов для '{target_loadout}': {count}.\n\n"
    "Скачать и установить {download_count} отсутствующих элемент(ов) с сохраненными метаданными лоадаута сейчас?"
)
MSG_MISSING_NO_METADATA = "У {count} отсутствующих элемент(ов) нет метаданных Nexus, они будут просто перечислены."

# ===== loadout_system/ls_ui_dropdown.py =====
BTN_LOADOUTS = "Лоадауты"
TIP_LOADOUTS = (
    "1.) Начните с отключения всех модов, затем включите те, которые хотите для нового лоадаута.\n"
    "2.) Нажмите иконку сохранения, чтобы сохранить включенные моды в файл лоадаута.\n"
    " - Сохраненные лоадауты можно переключать из этого списка в любое время.\n"
    " - В Manage All у каждой строки лоадаута есть иконки переименования, копирования файла и загрузки.\n"
    " - Используйте 'Import from file', чтобы добавить лоадауты из другого JSON-файла.\n"
    " - Вы также можете удалять/редактировать информацию лоадаута через 'Manage All'."
)

# ===== loadout_system/ls_ui_widgets.py =====
TIP_LOADOUT_CHECKBOX = "Отметьте, чтобы включить этот лоадаут при использовании 'Load' или 'Merge' Loadout."
TIP_RENAME_LOADOUT = "Переименовать лоадаут"
TIP_COPY_FILE = "Копировать файл в буфер обмена"
TIP_DOWNLOAD_LOADOUT = "Скачать этот лоадаут"
TIP_DETECT_MISSING = (
    "Случайно удалили мод?\n"
    "Запустите это, чтобы обнаружить и скачать отсутствующие моды из этого лоадаута"
)
TIP_REFRESH_NEXUS = (
    "Проверить и обновить ссылки Nexus + ID файлов.\n"
    "Когда мод обновляется на Nexus, ID загрузки файла меняется, но старый ID может остаться в файле лоадаута.\n"
    "   - Устаревшие URL/ID могут приводить к ошибкам загрузки.\n"
    "Этот запуск проверит такие устаревшие записи и обновит их по последним данным Nexus.\n"
    "Запускайте это, если\n"
    "   - Вы недавно обновляли существующие моды (не добавляли/удаляли, только обновляли)\n"
    "   - Перед тем как делиться лоадаутом с другими."
)

# ===== loadout_system/ls_ui_manage_dialog.py =====
LBL_MANAGE_LOADOUTS_TITLE = "Файлы лоадаутов:"
LBL_MANAGE_LOADOUTS_DESC = "(введите имя ниже, затем нажмите 'Save Loadout', чтобы создать новый лоадаут)"
LBL_MANAGE_LOADOUTS_TIP_1 = "Совет 1: Выберите сохраненный лоадаут и нажмите 'Save Loadout', чтобы перезаписать его."
LBL_MANAGE_LOADOUTS_TIP_2 = "Совет 2: Наведите курсор на кнопки для информационных подсказок."
LBL_CREATE_LOADOUT = "Создать лоадаут:"
BTN_SAVE_LOADOUT = "Save Loadout"
BTN_LOAD_SELECTED = "Загрузить выбранные"
BTN_MERGE_SELECTED = "Объединить выбранные"
BTN_IMPORT_LOADOUT = "Импорт лоадаута"
BTN_DELETE_LOADOUT = "Удалить лоадаут"

TIP_OPEN_LOADOUTS_FOLDER = "Открыть папку лоадаутов"
TIP_SAVE_LOADOUT = (
    "- Введите новое имя и нажмите 'Save Loadout', чтобы создать новый лоадаут \n"
    "- Выберите существующий лоадаут и нажмите 'Save Loadout', чтобы перезаписать"
)
TIP_LOAD_LOADOUT = (
    "Загрузить (включить) один или несколько лоадаутов.\n"
    " Только включенные моды, которые сейчас установлены.\n"
    " Используйте кнопку загрузки, чтобы действительно скачать файлы списка модов. \n"
    " Вы также можете загрузить лоадаут, затем нажать F9 для поиска отсутствующих файлов модов."
)
TIP_MERGE_LOADOUT = "Объединить выбранные лоадауты в один новый лоадаут."
TIP_IMPORT_LOADOUT = "Импортировать лоадауты из JSON-файла."
TIP_DELETE_LOADOUT = "Удалить выбранный лоадаут."
DLG_TITLE_OVERWRITE_LOADOUT = "Перезаписать лоадаут"
MSG_OVERWRITE_LOADOUT = "Перезаписать существующий лоадаут '{name}'?"
DLG_TITLE_COPY_LOADOUT = "Копировать файл лоадаута"
DLG_TITLE_DOWNLOAD_LOADOUT = "Скачать лоадаут"
DLG_TITLE_REFRESH_NEXUS = "Обновить метаданные Nexus"
MSG_NEXUS_API_REQUIRED = "Требуется API-ключ Nexus."
MSG_REFRESH_NEXUS_CONFIRM = "Проверить ссылки Nexus и закрепленные ID файлов для '{loadout_name}' и перезаписать этот файл лоадаута обновленными метаданными?"
MSG_REFRESH_NO_ENTRIES = "В этом лоадауте нет записей метаданных. Сначала сохраните или импортируйте метаданные."
MSG_REFRESH_WRITE_ERROR = "Проверка завершена, но не удалось записать файл:\n{error}"
MSG_REFRESH_COMPLETE = (
    "Обновление завершено для '{loadout_name}'.\n\n"
    "Проверено: {scanned_count}\n"
    "Валидно: {valid_count}\n"
    "Невалидно: {invalid_count}\n"
    "Исправлено мертвых ID: {repaired_count}\n"
    "Обновлено записей (всего): {changed}\n"
)
DLG_TITLE_LOADOUTS = "Лоадауты"
MSG_MULTI_SELECT_ONLY_DELETE = "При множественном выборе доступны только действия удаления.\n\nЗапрошенное действие: {action_label}"
MSG_OVERWRITE_PIN_MODE = "Перезаписать существующий лоадаут '{name}' текущими включенными модами?\n\nВыберите, как обрабатывать выбор ID файлов для модов в этом лоадауте:\n\n"
BTN_UPDATE_ALL = "Обновить все"
BTN_UPDATE_NEW = "Обновить новые"
BTN_DONT_UPDATE = "Не обновлять"
MSG_SELECT_ONE_OVERWRITE = "Выберите только один лоадаут для перезаписи или введите новое имя."
MSG_ENTER_LOADOUT_NAME = "Введите имя лоадаута или выберите один лоадаут для перезаписи."
DLG_TITLE_SAVE_LOADOUT = "Сохранить лоадаут"
MSG_PIN_FILE_IDS_PROMPT = (
    "У некоторых модов на Nexus доступно несколько основных или опциональных файлов.\n"
    "Хотите сохранить конкретную версию файла в этом лоадауте?\n\n"
    "Это сделает загрузку/обмен лоадаутом более предсказуемыми в будущем.\n\n"
    "Примечание: CZT покажет вам каждый доступный вариант для удобного выбора. Ничего вручную искать не нужно.\n"
)
MSG_OVERWRITE_SAVED = "Перезапись сохранена.\n\nИспользованный режим: {mode_label}\nОбновлено ID файлов: {processed}"
MSG_OVERWRITE_SAVED_NO_CHANGE = "Перезапись сохранена.\n\nИспользованный режим: {mode_label}\n0 записей обновлено. Новые данные совпали с существующими."
MSG_SELECT_LOADOUTS_DELETE = "Выберите один или несколько сохраненных лоадаутов для удаления."
DLG_TITLE_DELETE_LOADOUTS = "Удалить лоадауты"
MSG_CHECK_LOADOUTS_LOAD = "Отметьте один или несколько сохраненных лоадаутов для загрузки."
DLG_TITLE_LOAD_LOADOUT = "Загрузить лоадаут"
MSG_LOADED_LOADOUTS = "Лоадаут{plural} успешно загружен(о): {count}."
DLG_TITLE_MERGE_LOADOUTS = "Объединить лоадауты"
MSG_SELECT_TWO_MERGE = "Выберите минимум два сохраненных лоадаута для объединения."
LBL_MERGED_LOADOUT_NAME = "Имя объединенного лоадаута:"
MSG_ENTER_MERGED_NAME = "Введите корректное имя объединенного лоадаута."
DLG_TITLE_RENAME_LOADOUT = "Переименовать лоадаут"
LBL_NEW_FILE_NAME = "Новое имя файла:"

# ===== loadout_system/download_list.py =====
DLG_TITLE_DOWNLOAD_MOD_LIST = "Скачать список модов"
MSG_RUN_INSTALL_NOW = "{summary_text}\n\nЗапустить установку сейчас?"
MSG_INSTALL_NOT_AVAILABLE = "Логика установки недоступна"

# ===== loadout_system/importing.py =====
DLG_TITLE_IMPORT_LOADOUTS = "Импорт лоадаутов"
MSG_IMPORT_ROOT_NOT_SET = "Корневая папка не настроена."

# ===== nexus/updates.py =====
MSG_API_KEY_REQUIRED = (
    "Для проверки обновлений требуется ваш API-ключ Nexus.\n"
    "API-ключ используется для связи с сайтом Nexus.\n"
    " Ключ сохраняется локально в вашем файле конфига."
)
MSG_NO_TRACKED_MODS = "Для этого профиля не найдено отслеживаемых модов."
MSG_ALL_UP_TO_DATE = "Все моды актуальны!"
LBL_UPDATES_AVAILABLE = "Доступно обновлений:"
UPDATE_LINE_FMT = "→ {mod_name} (Текущая: {local_version} | Новая: {latest_version})"

# ===== nexus/nexus_sync.py =====
MSG_MOD_DIR_NOT_SET = (
    "Папка модов не задана или не существует. "
    "Перед сохранением ссылок Nexus настройте папку модов во вкладке User Settings."
)
MSG_NEXUS_INFO_UPDATED = "Информация Nexus обновлена для модов: {count}."

# ===== nexus/downloads.py =====
LBL_SELECT_FILE_DOWNLOAD = "Выберите файл для загрузки"
LBL_SELECT_A_FILE = "Выберите файл для загрузки..."
BTN_DOWNLOAD = "Скачать"
ERR_DOWNLOAD_CANCELLED = "Загрузка отменена"
ERR_NO_FILE_SELECTED = "Файл не выбран"
ERR_MISSING_API_KEY = "Отсутствует API-ключ Nexus"
ERR_NO_FILES_AVAILABLE = "Нет доступных файлов"
ERR_MISSING_MOD_ID_URL = "Отсутствует Nexus Mod ID или URL"
ERR_CANNOT_RESOLVE_SLUG = "Не удалось определить Nexus slug игры для этого профиля"
ERR_INVALID_MOD_ID_URL = "Некорректный Nexus Mod ID или URL"
ERR_NO_DOWNLOADABLE_FILE = "Нет ID загружаемого файла"
ERR_MISSING_ROOT_FOLDER = "Отсутствует czt_root_folder"
ERR_NO_SELECTED_MODS = "Нет выбранных модов"
ERR_NO_TRACKED_MODS_PROFILE = "Нет отслеживаемых модов для текущего профиля"
ERR_NO_VALID_NEXUS_URL = "Среди выбранных модов нет валидного nexus_url"
LBL_INSTALLED_MOD = "Установленный мод: {name}"
LBL_INSTALLED_FILE = "Установленный файл: {name}"
LBL_FILE_UNKNOWN = "Неизвестно"
LBL_FILE_VERSION = "Версия {version}"

# ===== nexus/browse_mods/browser_actions.py =====
MSG_OPEN_MOD_PAGE_FIRST = (
    "Сначала откройте конкретную страницу мода Nexus, затем нажмите Add Current Mod.\n\n"
    "Ожидаемый формат URL:\n"
    "https://www.nexusmods.com/<game>/mods/<id>"
)
STATUS_DOWNLOADING_MOD = "Скачивание мода {mod_id}..."
STATUS_DOWNLOAD_FAILED = "Ошибка загрузки"
STATUS_DOWNLOAD_INSTALLING = "Загрузка завершена. Установка..."
STATUS_DOWNLOADED = "Скачано: {name}"
MSG_DOWNLOAD_COMPLETE_SAVED = "Загрузка завершена.\n\nСохранено в: {path}"
STATUS_INSTALL_FAILED = "Ошибка установки"
STATUS_INSTALLED = "Установлено: {name}"

# ===== nexus/browse_mods/browser_widgets.py =====
LBL_SELECT_A_MOD = "Выберите мод"
LBL_NOT_INSTALLED = "Не установлен"
BTN_ADD_TO_FAVORITES = "Добавить в избранное"
LBL_ZERO_DOWNLOADS = "0 загрузок"
LBL_ZERO_ENDORSEMENTS = "0 одобрений"
LBL_UPDATED_NONE = "Обновлено: --"
LBL_NO_MOD_SELECTED = "Мод не выбран"
LBL_PAK_FILES = "Pak-файлы"
LBL_NO_FILES_AVAILABLE = "Нет доступных файлов"
LBL_NO_CHANGELOG = "История изменений отсутствует"
LBL_BY_AUTHOR = "Автор: {author}"
LBL_DOWNLOADS_COUNT = "Загрузок: {count}"
LBL_ENDORSEMENTS_COUNT = "Одобрений: {count}"
LBL_UPDATED_DATE = "Обновлено {date}"
LBL_NO_DESCRIPTION = "Описание отсутствует."
LBL_UNKNOWN_MOD = "Неизвестный мод"

# ===== nexus/browse_mods/browser_window.py =====
DLG_TITLE_BROWSE_NEXUS = "Обзор Nexus Mods - {profile}"
TIP_BACK = "Назад"
TIP_FORWARD = "Вперед"
TIP_REFRESH = "Обновить"
TIP_GO = "Перейти"
TIP_ENDORSEMENT_STATUS = "Статус одобрения"
MSG_WEBENGINE_UNAVAILABLE = (
    "Qt WebEngine недоступен в этой установке.\n"
    "Установите PySide6-WebEngine для встроенного просмотра Nexus."
)
STATUS_BROWSER_UNAVAILABLE = "Встроенный браузер недоступен"
STATUS_LOADING_PAGE = "Загрузка страницы..."
STATUS_NO_NEXUS_LINK = "Для этого профиля не настроена ссылка игры Nexus"
STATUS_LOADING_MODS = "Загрузка модов Nexus..."
STATUS_PAGE_LOADED = "Страница загружена"
STATUS_PAGE_FAILED = "Не удалось загрузить страницу"

# ===== nexus/browse_mods/endorsements.py =====
TIP_ENDORSE_ONLY_MOD_PAGES = "Статус одобрения доступен только на страницах модов"
TIP_ENDORSED = "Одобрено"
TIP_NOT_ENDORSED = "Не одобрено"
ERR_INVALID_ENDORSEMENT = "Некорректное действие одобрения"
ERR_UNKNOWN_ENDORSEMENT = "Неизвестная ошибка одобрения"
STATUS_OPEN_MOD_TO_ENDORSE = "Откройте конкретную страницу мода для одобрения"
STATUS_ENDORSE_UNAVAILABLE = "Статус одобрения недоступен"
STATUS_UPDATING_ENDORSEMENT = "Обновление одобрения..."
STATUS_ENDORSED = "Одобрено"
STATUS_ENDORSEMENT_REMOVED = "Одобрение удалено"
STATUS_ENDORSEMENT_FAILED = "Не удалось выполнить одобрение"
MSG_ENDORSEMENT_FAILED = "Не удалось обновить одобрение.\n\n{error}"

# ===== nexus/browse_mods/install_state.py =====
LBL_MOD_INSTALLED = "Мод установлен"
LBL_MOD_NOT_INSTALLED = "Мод не установлен"

# ===== nexus/protocol_handler/nxm/nxm_actions.py =====
MSG_NXM_GAME_MISMATCH = (
    "Этот мод для \"{game}\". \n"
    "Текущий профиль: \"{profile}\".\n\n"
    "Переключитесь на профиль \"{game}\", затем попробуйте снова."
)

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py =====
MSG_CZTMM_GAME_MISMATCH = (
    "Мод, который вы попытались установить, предназначен для \"{game}\". \n"
    "Ваш текущий профиль: \"{profile}\".\n\n"
    "Переключитесь на профиль \"{game}\", затем попробуйте снова."
)

# ===== refresh_manager/refresh_manager.py =====
PLACEHOLDER_SEARCH_MODS = "Поиск модов : {profile}"


# =====================================================================
#  СООБЩЕНИЯ ЛОГА  (czt_log / czt_log_synced)
# =====================================================================

# ===== install_mods/process_install.py (логи) =====
LOG_INSTALL_CANCELLED = "[INSTALL CANCELLED] Установка отменена пользователем во время подтверждения замены."
LOG_INSTALL_FAILED = "\n[ERROR] Установка не удалась: {error}\n"
LOG_INSTALL_QUEUED = "[INSTALL] Уже выполняется другая установка. Запрос поставлен в очередь."
LOG_INSTALL_SELECTED_FILES = "\n[INSTALL] Выбранные файлы:\n{file_list}"
LOG_PROCESSING_MOD = "[PROCESSING] Мод: {install_label}"
LOG_INSTALL_MOD_FAILED = "[ERROR] Ошибка при установке '{install_label}': {error}"
LOG_DELETE_SOURCE_FAILED = "[DELETE AFTER INSTALLED] Не удалось удалить исходный элемент '{src_path}': {error}"
LOG_INSTALL_COMPLETED = " \n[INSTALL PROCESS COMPLETED] Все выбранные моды обработаны.\n"
LOG_SUMMARY = "[SUMMARY]"
LOG_SUMMARY_SUCCESS = "\n    > УСПЕШНО: "
LOG_SUMMARY_FAILED = "\n    > ОШИБКА: "
LOG_SUMMARY_SKIPPED = "\n    > ПРОПУЩЕНО: (кандидат архива, совпавший с exporter, не найден) "
LOG_SUMMARY_SOURCE_DELETED = "\n    > ИСХОДНЫЙ ФАЙЛ УДАЛЕН: "
LOG_SUMMARY_SOURCE_DELETE_SKIPPED = "\n    > УДАЛЕНИЕ ИСХОДНОГО ФАЙЛА ПРОПУЩЕНО: пользователь отклонил подтверждение."

# ===== install_mods/process_uninstall.py (логи) =====
LOG_DELETED_MODS = "[DELETE] Удалено модов: {count}:\n -> {item_list}"

# ===== install_mods/dying_light_auto_patch.py (логи) =====
LOG_DL_SLOT_SKIPPED = "[DL DATA SLOT] '{base_name}' пропущен: цель замены не выбрана, а текущий слот недоступен."
LOG_DL_SLOT_KEEP = "[DL DATA SLOT] Для установки сохранено исходное имя файла '{base_name}'."
LOG_DL_SLOT_INSTALL_NEW = "[DL DATA SLOT] Выбрана установка как новый: следующий свободный слот '{selected_file_name}' для '{base_name}'."
LOG_DL_SLOT_REPLACE = "[DL DATA SLOT] Для '{base_name}' выбрана цель замены '{selected_file_name}'."

# ===== install_mods/archive_handler/archive_handler_core.py (логи) =====
LOG_OPTION_SKIP_NO_EXPORTERS = "[INSTALL][OPTION][SKIPPED] Нет exporter basenames для кандидатов {choice_kind} в {archive_name}."
LOG_OPTION_AUTO_SELECT = "[INSTALL][OPTION] Автовыбрано кандидат(ов) {count} {choice_kind}, совпавших с exporter, в {archive_name}."
LOG_OPTION_SKIP_NO_MATCH = "[INSTALL][OPTION][SKIPPED] В {archive_name} не найдено кандидатов {choice_kind}, совпавших с exporter."
LOG_CACHE_SKIP = "[INSTALL][OPTION][CACHE] Использована кэш-опция файла: пропустить архив {archive_name}"
LOG_CACHE_INSTALL_ALL = "[INSTALL][OPTION][CACHE] Использована кэш-опция файла: установить все из архива {archive_name}"
LOG_CACHE_SELECTED = "[INSTALL][OPTION][CACHE] Использован кэшированный выбор файла: {chosen_rel}"
LOG_MULTI_FOLDER_CANDIDATES = "[INSTALL][OPTION] В архиве найдено несколько папок-кандидатов: {archive_name}"
LOG_SKIPPED_FOLDER_CHOICE = "[INSTALL][SKIPPED] Пользователь пропустил выбор папки архива: {archive_name}"
LOG_ADDITIONAL_FOLDER_CANDIDATES = "[INSTALL][OPTION] В выбранной опции найдены дополнительные папки-кандидаты: {archive_name}"
LOG_SKIPPED_NESTED_FOLDER = "[INSTALL][SKIPPED] Пользователь пропустил выбор вложенной папки: {archive_name}"
LOG_MULTI_FILE_CANDIDATES = "[INSTALL][OPTION] В архиве найдено несколько кандидатов для установки: {archive_name}"
LOG_SKIPPED_FILE_CHOICE = "[INSTALL][SKIPPED] Пользователь пропустил выбор установки архива: {archive_name}"
LOG_ADDITIONAL_FILE_CANDIDATES = "[INSTALL][OPTION] В выбранной опции найдены дополнительные кандидаты файлов: {archive_name}"
LOG_SKIPPED_NESTED_FILE = "[INSTALL][SKIPPED] Пользователь пропустил выбор вложенного файла: {archive_name}"
LOG_UNSUPPORTED_ARCHIVE = "[ERROR] Неподдерживаемый тип архива или отсутствует библиотека: {archive_type}"
LOG_RAR_NOT_AVAILABLE = "[ERROR] Библиотека rarfile недоступна для распаковки .rar: {archive_name}."
LOG_7Z_NOT_AVAILABLE = "[ERROR] Библиотека py7zr недоступна для распаковки .7z: {archive_name}"
LOG_PROCESS_ITEM_FAILED = "[ERROR] Не удалось обработать {item}: {error}"
LOG_EXTRACT_FAILED = "[ERROR] Не удалось распаковать {archive_type} {archive_name}: {error}"

# ===== install_mods/replacement_handler/resolve_replacement.py (логи) =====
LOG_REPLACEMENT_CONFIRM = "[INSTALL SAFETY] Требуется подтверждение замены для '{mod_name}'"
LOG_REPLACEMENT_REMOVE_FAILED = "[WARN] Не удалось удалить выбранный файл замены '{old_path}': {error}"
LOG_REPLACEMENT_DIALOG_FAILED = "[WARN] Сбой диалога подтверждения замены: {error_type}: {error}"

# ===== install_mods/install_registry.py (логи) =====
LOG_REPLACE_EXISTING = "[UPDATE INSTALL] Заменен существующий файл мода: {old_file} -> {new_file}"
LOG_REPLACE_REMOVE_FAILED = "[WARN] Не удалось удалить замененный файл мода '{old_file}': {error}"
LOG_REPLACE_DISABLED_REMOVE_FAILED = "[WARN] Не удалось удалить замененный отключенный файл мода '{old_file}': {error}"
LOG_JSON_UPDATING = "[JSON WRITE] Обновление существующей записи в списке модов:\n   ↳'{mod_name}'"
LOG_REPLACE_OPTIONS_FOUND = "[REPLACE] '{mod_name}': найдено вариантов существующих файлов: {count}."
LOG_INSTALLED = "[INSTALLED] '{mod_name}'"
LOG_INSTALLED_KEPT_EXISTING = "[INSTALLED] '{mod_name}': сохранены существующие файлы и установлен новый файл."
LOG_JSON_WRITE_COMPLETE = (
    "[JSON WRITE COMPLETE] profile_mods_list.json успешно обновлен.\n"
    "[SUMMARY] Обновлено: {updated_count}, Новых: {new_count}, Всего: {total_count}."
)
LOG_JSON_WRITE_ERROR = "[ERROR] Не удалось обновить список модов: {error}"

# ===== install_mods/install_utilities.py (логи) =====
LOG_STAGING_ERROR = "[STAGING ERROR] Не удалось подготовить {file_name}: {error}"
LOG_STAGED = "[STAGED] Подготовлено модов: {count} в:\n -> {staged_list}\n[SOURCE] -> {mods_source}"
LOG_REPLACEMENT_TIMEOUT = "[WARN] Истекло время ожидания диалога подтверждения замены."

# ===== install_mods/archive_handler/progress.py (логи) =====
LOG_PROGRESS = "[{stage_key}] {label} [{percent}%]"
LOG_EXTRACTING = "[EXTRACTING] {label} [0%]"
LOG_INSTALLING_PROGRESS = "[INSTALLING] {label} [0%]"

# ===== nexus/updates.py (логи) =====
LOG_UPDATE_SCAN_START = "[UPDATE SCAN] Текущий профиль: {profile_name} | Проверка доступных обновлений...\n"
LOG_UPDATE_SCAN_MOD = "→ Мод: {file_name} | Локальная: {local_version} | Последняя: {latest_version} | "
LOG_UPDATE_SCAN_COMPLETED = " \n[UPDATE SCAN COMPLETED] {scan_label} | найдено обновлений: {updated_count}"
LOG_UPDATE_SCAN_COMPLETED_ALT = "\n[UPDATE SCAN COMPLETED] {scan_label} | найдено обновлений: {updated_count}"

# ===== nexus/nexus_sync.py (логи) =====
LOG_NEXUS_MODS_DIR_MISSING = "[NEXUS] mods_dir отсутствует, используется резервный: {fallback_dir}"
LOG_NEXUS_MODS_DIR_ERROR = "[NEXUS][ERROR] mods_dir некорректен. Передано: {mods_dir} | Резервный: {fallback_dir} | Профиль: {profile_name}"
LOG_NEXUS_SAVING = "[NEXUS][SAVE] Сохранение собранных данных модов в {tracked_file}"
LOG_NEXUS_INFO_UPDATED_LOG = "[NEXUS] информация обновлена для модов: {updated_count}."

# ===== nexus/downloads.py (логи) =====
LOG_NEXUS_REDIRECT_STANDARD = "[NEXUS - STANDARD] Перенаправление на страницу файлов мода для загрузки: {target_url}"
LOG_NEXUS_OPEN_FAILED = "[NEXUS] Не удалось открыть страницу файлов мода: {error}"
LOG_DOWNLOADING = "[DOWNLOADING] {out_path}"
LOG_DOWNLOAD_FAILED = "[DOWNLOAD] Сбой для '{display_label}': {error}"
LOG_DOWNLOAD_COMPLETED = "[DOWNLOAD] Завершено: скачано файлов: {downloaded}."

# ===== nexus/browse_mods/browser_window.py (логи) =====
LOG_BROWSER_CLOSED = "[NEXUS_BROWSER] Закрыт"
LOG_BROWSER_NO_GAME = "[NEXUS_BROWSER] Нет доступной game_var"

# ===== nexus/protocol_handler/nxm/nxm_actions.py (логи) =====
LOG_NXM_RECEIVED = "[NXM] Получен URL: {nxm_url}"
LOG_NXM_PARSE_FAILED = "[NXM][ERROR] Не удалось разобрать NXM URL: {nxm_url}"
LOG_NXM_GAME_MISMATCH_LOG = "[NXM] Несовпадение игры: NXM={game_slug}, активный профиль={profile_game_slug}"
LOG_NXM_DOWNLOAD_EVENT = (
    "[NXM] Получено событие загрузки Nexus: Игра: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[NXM] CZT автоматически установит ваш файл после завершения загрузки.\n"
    "[NXM] Пожалуйста, подождите..."
)
LOG_NXM_DOWNLOAD_FAILED = "[NXM] Загрузка не удалась или была отменена"
LOG_NXM_DOWNLOAD_COMPLETE = "[NXM] Загрузка завершена: {result}"

# ===== nexus/protocol_handler/cztmm/cztmm_runtime.py (логи) =====
LOG_CZTMM_RECEIVED = "[CZTMM] Получен URL: {cztmm_url}"
LOG_CZTMM_PARSE_FAILED = "[CZTMM][ERROR] Не удалось разобрать URL: {cztmm_url}"
LOG_CZTMM_GAME_MISMATCH_LOG = "[CZTMM] Несовпадение игры: CZTMM={game_slug}, текущий профиль={profile_game_slug}"
LOG_CZTMM_DOWNLOAD_EVENT = (
    "[CZTMM] Получено событие загрузки Nexus: Игра: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[CZTMM] CZT автоматически установит ваш файл после завершения загрузки.\n"
    "[CZTMM] Пожалуйста, подождите..."
)
LOG_CZTMM_DOWNLOAD_EVENT_STANDARD = (
    "[CZTMM] Получено событие загрузки Nexus: Игра: {game_slug}, Mod ID: {mod_id}, File ID: {file_id}\n"
    "[CZTMM] [ОБНАРУЖЕН СТАНДАРТНЫЙ АККАУНТ NEXUS] \n"
    "[CZTMM] Не забудьте нажать 'Slow Download' в браузере!\n"
    "[CZTMM] CZT автоматически установит ваш файл после завершения загрузки.\n"
    "[CZTMM] Пожалуйста, подождите...\n"
)

# ===== nexus/account_type_status.py (логи) =====
LOG_NEXUS_ACCOUNT_TIER_FAILED = "[CZTMM] Не удалось определить уровень аккаунта Nexus, используется standard: {error}"

# ===== nexus/manual_download_install.py (логи) =====
LOG_NO_DOWNLOAD_DETECTED = "[CZTMM] Недавняя завершенная загрузка не обнаружена; автоустановка пропущена."
LOG_INSTALLING_DOWNLOAD = "[CZTMM] Установка загруженного файла: {chosen_path}"

# ===== nexus/browse_mods/browser_ext.py (логи) =====
LOG_BROWSER_JS_WITH_SOURCE = "[NEXUS_BROWSER][JS] {text} ({source}:{line_number})"
LOG_BROWSER_JS = "[NEXUS_BROWSER][JS] {text}"

# ===== nexus/browse_mods/marquee_label.py =====
BANNER_TEXT_FREE = (
	"Обнаружен стандартный аккаунт Nexus — "
	"Эта функция рассчитана на премиум-аккаунты — "
	"Прямые загрузки из удаленных приложений ограничены Nexus для бесплатных аккаунтов — "
	"Nexus применяет те же ограничения к Vortex."
)
BANNER_TEXT_PREMIUM = (
	"Для просмотра и загрузки модов вход в аккаунт не нужен, для этого и используется API-ключ в меню setup "
	"— Чтобы использовать этот браузер, перейдите на страницу нужного мода и нажмите кнопку 'Download + Install Current Mod' "
	"— Информация о моде сохраняется в локальный файл списка модов во время загрузки"
)
LOG_ACCOUNT_TIER_FALLBACK = "[NEXUS_BROWSER] Не удалось определить уровень аккаунта, используется free: {error}"

# ===== nexus/protocol_handler/nxm/nxm_runtime.py (логи) =====
LOG_NXM_STARTUP_REG_FAILED = "[NXM] Не удалось применить параметр регистрации при запуске: {error}"
LOG_NXM_SENT_URL = "[NXM] URL отправлен в запущенный экземпляр: {protocol_url_arg}"
LOG_NXM_SEND_FAILED = "[NXM] Не удалось отправить URL в запущенный экземпляр: {error}"
LOG_NXM_IPC_FAILED = "[NXM][ERROR] Не удалось запустить NXM IPC сервер"

# ===== working/multi_download_progress_dialog.py & download_progress_session.py =====
DLG_TITLE_DOWNLOADING_MODS    = "Скачивание модов"
DLG_TITLE_DOWNLOADING_UPDATES = "Скачивание обновлений модов"
LBL_DOWNLOAD_ROW_DEFAULT      = "Загрузка #{num}"
LBL_DOWNLOADS_COMPLETE        = "{done} / {total} загрузок завершено"
LBL_DOWNLOADS_REMAINING       = "Осталось в очереди: {count}"

# ===== install_mods/consolidated_install_dialog.py & закрепление файлов лоадаута =====
DLG_TITLE_RESOLVE_INSTALL     = "Решить варианты установки"
DLG_TITLE_SELECT_FILES_PIN    = "Выберите файлы для закрепления"
LBL_RESOLVE_HEADER            = "{count} мод(ов) требуют внимания.\nСделайте выбор ниже и нажмите «Применить»."
LBL_HDR_MOD_ARCHIVE           = "Архив мода:"
LBL_HDR_INSTALLED_MOD         = "Установленный мод:"
LBL_HDR_CHOOSE_DOWNLOAD       = "Выберите файл для загрузки:"
LBL_HDR_SELECT_LOADOUT_FILE   = "Выберите файл для лоадаута:"
LBL_HDR_ARCHIVE_OPTIONS       = "Опции архива: (выберите файл для установки)"
LBL_HDR_REPLACE_OR_NEW        = "Заменить существующий файл или установить как новый:"
LBL_UNKNOWN_MOD_INLINE        = "(неизвестно)"
LBL_FILE_NUM                  = "Файл {file_id}"
OPT_SKIP_DOWNLOAD             = "(пропустить загрузку)"
OPT_INSTALL_NEW               = "(установить как новый)"
OPT_INSTALL_ALL               = "Установить все"
OPT_SKIP                      = "Пропустить"
MSG_BROKEN_LINK               = "(ссылка недоступна — скачайте вручную)"
MSG_BROKEN_LINK_URL           = "(ссылка недоступна — см. {url})"
BTN_APPLY                     = "Применить"
BTN_SKIP_ALL                  = "Пропустить все"
BTN_USE_THIS_FILE             = "Использовать этот файл"
BTN_SELECT_FILE               = "Выбрать файл"
LBL_PIN_SELECT_HEADER         = "Выберите файл для закрепления"
LBL_CTX_MOD_NAME              = "Название мода: {name}"
LBL_CTX_LOADOUT               = "Лоадаут: {name}"
LBL_CTX_INSTALLED_FILE        = "Установленный файл: {name}"
LBL_CTX_MOD_FILE              = "Файл мода: {name}"
LBL_MOD_FALLBACK              = "Мод {mod_id}"
LBL_TARGET_UNKNOWN            = "неизвестно"


# ===== nexus/protocol_handler/nxm/nxm_register.py (логи) =====
LOG_NXM_REGISTERED = "[NXM] Зарегистрирован обработчик протокола nxm://: {command}"
LOG_NXM_REGISTER_FAILED = "[NXM][ERROR] Не удалось зарегистрировать обработчик nxm://: {error}"
LOG_NXM_UNREGISTERED = "[NXM] Удалена регистрация обработчика протокола nxm://"
LOG_NXM_UNREGISTER_FAILED = "[NXM][ERROR] Не удалось удалить регистрацию обработчика nxm://: {error}"

# ===== nexus/protocol_handler/cztmm/cztmm_register.py (логи) =====
LOG_CZTMM_REGISTERED = "[CZTMM] Зарегистрирован обработчик протокола cztmm://: {command}"
LOG_CZTMM_REGISTER_FAILED = "[CZTMM][ERROR] Не удалось зарегистрировать обработчик cztmm://: {error}"
LOG_CZTMM_UNREGISTERED = "[CZTMM] Удалена регистрация обработчика протокола cztmm://"
LOG_CZTMM_UNREGISTER_FAILED = "[CZTMM][ERROR] Не удалось удалить регистрацию обработчика cztmm://: {error}"

# ===== loadout_system/ls_ui_manage_dialog.py (логи) =====
LOG_LOADOUT_ROOT_NOT_SET = "[LOADOUT] Корневая папка не задана. Невозможно управлять лоадаутами."

# ===== loadout_system/download_list.py (логи) =====
LOG_LOADOUT_SAVE_FAILED_DL = "[LOADOUT] Не удалось сохранить импортированные лоадауты из Download Mod List."
LOG_LOADOUT_IMPORTED_DL = "[LOADOUT] Импортировано лоадаутов: {added_count} в сохраненные лоадауты профиля '{profile_name}' из Download Mod List."
LOG_DOWNLOAD_CANCELED = "[LOADOUT DOWNLOAD] Download Mod List отменен на этапе подтверждения повторной загрузки."
LOG_DOWNLOAD_SUMMARY = "[SUMMARY] Скачано: {downloaded} | Пропущено существующих: {skipped} | Ошибок: {failed}"
LOG_DOWNLOAD_INSTALL_QUEUED = "[INSTALL] Уже выполняется другая внутренняя download-install задача. Запрос поставлен в очередь."
LOG_DOWNLOAD_INSTALL_FAILED = "[INSTALL] Рабочий поток download-install завершился с ошибкой: {error}\n{traceback}"
LOG_LOADOUT_AUTO_SELECT_FAILED = "[LOADOUT] Не удалось автоматически выбрать импортированный лоадаут '{loadout_name}': {error}"

# ===== loadout_system/importing.py (логи) =====
LOG_LOADOUT_IMPORTED = (
    "[LOADOUT] Импортировано лоадаутов: {added_count} из '{imported_path}'. \n"
    "Записей добавлено в основной список модов: {profile_metadata_added}. \n"
    "Записей обновлено в основном списке модов: {profile_metadata_updated}."
)

# ===== loadout_system/build_loadout.py (логи) =====
LOG_LOADOUT_MERGE_FAILED = "[LOADOUT] Не удалось сохранить объединенные лоадауты для профиля '{profile_name}': {error}"

# ===== loadout_system/apply_loadout.py (логи) =====
LOG_LOADOUT_ROOT_NOT_SET_APPLY = "[LOADOUT] Корневая папка не задана. Невозможно применить лоадаут."
LOG_LOADOUT_NO_MODS = "[LOADOUT] Для лоадаута '{loadout_name}' моды не найдены."
LOG_LOADOUT_ROOT_NOT_SET_APPLY_MULTI = "[LOADOUT] Корневая папка не задана. Невозможно применить лоадауты."
LOG_LOADOUT_NO_MODS_MULTI = "[LOADOUT] Для выбранных лоадаутов моды не найдены."

# ===== loadout_system/storage.py (логи) =====
LOG_LOADOUT_REMOVE_FAILED = "[LOADOUT] Не удалось удалить существующие файлы лоадаутов: {error}"
LOG_LOADOUT_SAVE_FAILED = "[LOADOUT] Не удалось сохранить лоадауты: {error}"

# ===== loadout_system/select_file_variant.py (логи) =====
LOG_FILE_PIN_SKIPPED = "[LOADOUT] Закрепление файла пропущено для '{display_name}' ({cache_key}): {error}"

# ===== loadout_system/ls_utilities.py (логи) =====
LOG_FILE_CANDIDATES_FAILED = "[LOADOUT] Не удалось загрузить кандидаты файлов для {loadout_name}:{mod_id}: {error}"
LOG_FILE_PIN_SELECTION_SKIPPED = "[LOADOUT] Выбор закрепления файла пропущен для {loadout_name}:{mod_id}: {error}"

# ===== Get_SteamLibraries.py (логи) =====
LOG_STEAM_SCAN_DRIVE = "[STEAMLIB][SCAN] Сканирование диска {drive_root} на libraryfolders.vdf (UPDATED)"
LOG_STEAM_SCAN_LEGACY = "[STEAMLIB][SCAN] Сканирование диска {drive_root} на libraryfolder.vdf (LEGACY)"
LOG_STEAM_SEARCHING = "[STEAMLIB][SCAN] Поиск... {pattern}"
LOG_STEAM_LOCATED = "[STEAMLIB] [LOCATED] libraryfolders.vdf @ {vdf} (UPDATED)"
LOG_STEAM_LOCATED_LEGACY = "\n[STEAMLIB] [LOCATED] libraryfolder.vdf @ {vdf} (LEGACY)"
LOG_VDF_PARSING = "[VDF] Разбор VDF-файла..."
LOG_STEAM_ADDED = "[STEAMLIB][ADDED] ↾ {lib_common}"
LOG_STEAM_PARSE_WARN = "[WARN] Не удалось разобрать библиотеки Steam: {error}"
LOG_STEAM_SKIP_SCAN = "[STEAMLIB] Пропуск сканирования библиотек Steam: режим путей для '{current_profile}' = '{pathing_mode}'."
LOG_STEAM_RUN_UTIL = "[RUN UTIL] ▶ SteamLibrarySearchUtility ◀"
LOG_STEAM_SCANNING = "[STEAMLIB] Сканирование библиотек Steam..."
LOG_STEAM_SCAN_SUCCESS = "[STEAMLIB] [SCAN SUCCESSFUL]\n    ↾ Все пути библиотек Steam обновлены."
LOG_STEAM_WARN_NO_ROOT = "⚠️ [WARNING] Невозможно сохранить конфиг, потому что czt_root_folder не существует."
LOG_EXE_DETECTED = "[EXE DETECTED] Найдено @ {path}"
LOG_EXE_NOT_FOUND = "[EXE DETECT] Корректный exe не найден."
