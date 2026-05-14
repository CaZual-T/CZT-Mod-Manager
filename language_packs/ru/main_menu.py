# Вкладка Main Menu - Русские строки

# Общие
STATUS_GAME_NOT_DETECTED = "ИГРА НЕ ОБНАРУЖЕНА"

# Подсказки кнопок главной вкладки
TIP_BTN_GAME_BROWSE = "Открыть папку модов текущего профиля и папку назначения симлинков."
TIP_BTN_OPEN_CUSTOM_SETTINGS = "Параметры запуска и пользовательские настройки."
TIP_BTN_FIRST_TIME_SETUP = "Создать корень, установить UnRAR, задать API-ключ."
TIP_BTN_SELECT_ALL = "[ВЫБРАТЬ/СНЯТЬ ВЫБОР СО ВСЕХ]"
TIP_BTN_DELETE_SELECTED = (
    "Удалить выбранные мод(ы) из папки источника установки.\n"
    "> Это нельзя отменить! (перед удалением появится предупреждение)"
)
TIP_BTN_INSTALL_SELECTED = (
    "Установить выбранные мод(ы) вручную в текущий профиль.\n"
    "> Метаданные при ручной установке не сохраняются.\n"
    "   > Если устанавливаемый мод новый, после установки откройте вкладку менеджера,.. \n"
    "   > ...кликните по файлу правой кнопкой и задайте Nexus ID/URL вручную, чтобы CZT смог получить и сохранить метаданные.\n"
    "> Уже существующие моды можно безопасно переустанавливать для обновления.\n"
)
TIP_PATH_MODE_MANUAL = (
    "ВКЛЮЧЕНО = Пользователь может вручную задать путь к EXE и путь, куда моды будут подключаться при запуске.\n"
    "[ВАЖНО] Прочитайте лог, который появится после выбора этой опции, чтобы узнать подробности."
)
TIP_PATH_MODE_STEAM = (
    "ВКЛЮЧЕНО (ПО УМОЛЧАНИЮ) = CZT использует ваш STEAM library.vdf для автоматической настройки всех нужных путей.\n"
    "Нажмите 'Detect Steam' для автонастройки путей."
)
TIP_BTN_MANAGE_MODS = "Присоединяйтесь к Discord CZT Mod Manager для обновлений и поддержки."
TIP_BTN_CLEAN_MOD_LIST = (
    "4 опции:\n"
    "- Удалить существующие симлинки профиля.\n"
    "- Удалить логи мониторинга сбоев.\n"
    "- Удалить историю загрузок.\n"
    "- Удалить устаревшие записи в файле списка модов."
)
TIP_BTN_DONATIONS = "Спасибо за использование CZT!\nНажмите здесь, чтобы открыть страницу пожертвований (Paypal)"
TIP_BTN_UPDATE_CZT = (
    "Нажмите здесь, чтобы открыть инструкции CZT Mod Manager.\n\n"
    "[ГОРЯЧИЕ КЛАВИШИ]\n"
    "- Нажмите SHIFT + H, чтобы показать доступные горячие клавиши.\n"
    "- Нажмите F2, чтобы открыть меню порядка загрузки."
)

# Подписи главной вкладки
LBL_PATH_MODE_MANUAL = "Ручной"
LBL_PATH_MODE_STEAM = "Steam"
TAB_TITLE_MAIN_MENU = "Главное меню"

# Подписи кнопок/секций главной вкладки
LBL_PATH_MODES = "Режимы путей"
LBL_BTN_DETECT_STEAM = "Detect Steam"
LBL_BTN_SAVE_CONFIG = "Сохранить конфиг"
LBL_BTN_SET_INSTALL_DIRECTORY = "Задать папку установки"
LBL_BTN_SET_EXE_PATH = "Задать путь EXE"
LBL_BTN_LAUNCH_GAME = "Запустить игру"
LBL_BTN_BROWSE = "Обзор"
LBL_BTN_SETTINGS = "Настройки"
LBL_BTN_SETUP = "Настройка"
LBL_BTN_GUIDE = "Гайд"
LBL_BTN_DISCORD = "Discord"
LBL_BTN_CLEAN = "Очистка"
LBL_BTN_DONATIONS = "Пожертвования"
LBL_BTN_PATCH_NOTES = "История изменений"
TIP_BTN_PATCH_NOTES = "Просмотр истории изменений CZT Mod Manager и проверка обновлений."

# Подписи статистики хранилища
LBL_STORAGE_OVERVIEW = "[Обзор CZT]"
LBL_STATS_DISK_USAGE_TOTAL = "CZT - Использовано хранилища:"
LBL_STATS_MODS_ENABLED = "Включено модов: {count}"
LBL_STATS_MODS_DISABLED = "Отключено модов: {count}"
LBL_STATS_MODS_ENABLED_VALUE_FMT = "размер на диске: {size}"
LBL_STATS_MODS_DISABLED_VALUE_FMT = "размер на диске: {size}"
LBL_STATS_UPDATES_AVAILABLE = "Доступно обновлений: {count}"
LBL_STATS_APP_CPU_USAGE = "CZT - Загрузка CPU:"
LBL_STATS_APP_RAM_USAGE = "CZT - Использование RAM:"
LBL_STATS_NETWORK_SPEED = "Скорость сети:"
LBL_STATS_DISK_RW_SPEED = "Скорость чтения | записи:"
LBL_STATS_DISK_TRANSFER_RATE = "Скорость передачи:"
LBL_STATS_UPDATES_VALUE_FMT = "сканировано: {date}"
LBL_STATS_LAST_CHECKED_NEVER = "никогда"
LBL_STATS_NETWORK_VALUE_FMT = "↑ {sent} | ↓ {recv}"
LBL_STATS_DISK_RW_VALUE_FMT = "Ч {read} | З {write}"
LBL_STATS_DISK_TRANSFER_VALUE_FMT = "{total}"
LBL_STATS_UNAVAILABLE = "Недоступно"

TIP_STORAGE_OVERVIEW_CUSTOMIZE = "Нажмите, чтобы настроить виджеты обзора CZT: меняйте порядок строк или содержимое."
TIP_OVERVIEW_ITEM_UPDATES_AVAILABLE = "Показывает, сколько модов имеют доступные обновления.\n ↳ сканировано: (дата) - дата самого свежего полного/автоматического сканирования."
TIP_OVERVIEW_ITEM_MODS_ENABLED = "Включенные моды (количество) для текущего профиля:\n ↳ общий размер папки 'включенных' модов текущего профиля."
TIP_OVERVIEW_ITEM_MODS_DISABLED = "Отключенные моды (количество) для текущего профиля:\n ↳ общий размер папки 'отключенных' модов текущего профиля."
TIP_OVERVIEW_ITEM_DISK_USAGE_TOTAL = "Использовано хранилища CZT (размер корневой папки пользователя)\n / общая емкость диска, на котором находится корневая папка CZT."
TIP_OVERVIEW_ITEM_APP_CPU_USAGE = "Нагрузка CPU от CZT | общая нагрузка CPU системы | текущая частота CPU."
TIP_OVERVIEW_ITEM_APP_RAM_USAGE = "Использование RAM приложением CZT | общий объем RAM системы."
TIP_OVERVIEW_ITEM_NETWORK_SPEED = "Живая скорость отдачи и загрузки сети системы."
TIP_OVERVIEW_ITEM_DISK_RW_SPEED = "Живая скорость чтения и записи для выбранного диска (диск)."
TIP_OVERVIEW_ITEM_DISK_TRANSFER_RATE = "Живая суммарная скорость передачи чтение + запись для выбранного диска (диск)."

DLG_TITLE_STORAGE_WIDGETS = "Настроить обзор CZT"
DLG_STORAGE_WIDGETS_DESC = "Перетаскивайте элементы для изменения порядка. Отмеченные строки отображаются в обзоре CZT."
LBL_STORAGE_WIDGETS_DRIVE_LABEL = "Выберите диск для обзора Ч/З и скорости передачи:"
LBL_STORAGE_WIDGETS_DRIVE_ALL = "Все"
BTN_STORAGE_WIDGETS_RESTORE_DEFAULT = "Восстановить по умолчанию"
BTN_STORAGE_WIDGETS_CANCEL = "Отмена"
BTN_STORAGE_WIDGETS_APPLY = "Применить"
MSG_STORAGE_WIDGETS_NONE_SELECTED_TITLE = "Виджеты не выбраны"
MSG_STORAGE_WIDGETS_NONE_SELECTED_BODY = "Выберите хотя бы один виджет для отображения."
MSG_STORAGE_WIDGETS_TOO_MANY_TITLE = "Слишком много виджетов"
MSG_STORAGE_WIDGETS_TOO_MANY_BODY = "Эта панель поддерживает до {max_visible} видимых виджетов одновременно."

# Заголовки всплывающих окон главной вкладки
DLG_TITLE_CUSTOM_SETTINGS = "Пользовательские настройки"
DLG_TITLE_FIRST_TIME_SETUP = "Первоначальная настройка"

# Сообщения лога главной вкладки
LOG_ROOT_MISSING = (
    "\n❌ [ERROR] Корневая папка не задана/папка не существует! \n"
    "⚠️ [WARNING] Любые применяемые настройки не будут сохранены, пока корень не создан!\n"
    "❓ [HINT] Нажмите кнопку 'SETUP' выше...\n"
    "  1: Нажмите 'CREATE ROOT' и выберите предпочитаемый диск для создания нужных папок.\n"
    "  2: Нажмите 'INSTALL UNRAR' после создания корневых папок.\n"
    "    - Нажмите установку unrar еще раз после завершения, чтобы задать путь.\n"
    "  3: Перезапустите CZT после установки UnRAR.exe\n"
)

# Сообщения утилиты очистки
MSG_ROOT_NOT_SET_CLEAN = "Корневая папка не задана. Невозможно очистить список модов."
MSG_NO_VALID_INSTALL_DIR = (
    "Не задана корректная папка установки!\n \n- Режим путей [STEAM]:\n   > Нажмите 'Detect Steam'\n "
    "\n- Режим путей [Manual]:\n   > Нажмите 'SET INSTALL' и 'SET EXE' для настройки."
)
LOG_CLEAN_HISTORY_CLEARED = "[CLEAN] История в {history_path} очищена."
LOG_CLEAN_HISTORY_CLEAR_FAILED = "[CLEAN] Не удалось очистить {history_name} по пути {history_path}: {error}"
LOG_CLEAN_CRASH_LOG_CLEARED = "[CLEAN] Логи мониторинга сбоев очищены: {log_path}"
LOG_CLEAN_CRASH_LOG_CLEAR_FAILED = "[CLEAN] Не удалось очистить лог сбоя {log_name} по пути {log_path}: {error}"
LOG_CLEAN_MOD_LIST_UPDATE_FAILED = "[CLEAN] Не удалось обновить список модов: {error}"
LOG_CLEAN_STALE_ENTRIES_REMOVED = "[CLEAN] Удалено устаревших записей модов: {removed} из mod_list.json для профиля '{profile_name}'."
LOG_CLEAN_NO_OPTIONS_SELECTED = "[CLEAN] Опции не выбраны."
LOG_PER_FILE_SYMLINK_DISABLED = "[PER-FILE] Симлинк отключен: {path}"
LOG_PER_FILE_SYMLINK_REMOVE_FAILED = "[PER-FILE] Не удалось удалить симлинк {path}: {error}"
LOG_PER_FOLDER_LINK_DISABLED = "[PER-FOLDER] Симлинк/junction отключен: {path}"
LOG_PER_FOLDER_LINK_REMOVE_FAILED = "[PER-FOLDER] Не удалось удалить симлинк/junction {path}: {error}"
LOG_LINK_MODS_JUNCTION_DISABLED = "[LINK] Junction Mods отключен: {path}"
LOG_LINK_MODS_SYMLINK_DISABLED = "[LINK] Симлинк Mods отключен: {path}"
LOG_LINK_MODS_SYMLINK_REMOVE_FAILED = "[LINK] Не удалось удалить симлинк Mods: {error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED = "[CLEAN] Существующие симлинки профиля '{profile_name}' удалены."
LOG_CLEAN_EXE_TYPE_LINKS_REMOVED = "[{mod_type}] Отвязано модов: {count}."
LOG_CLEAN_TYPE_SYMLINKS_REMOVED = "[{mod_type}] Отвязано модов: {count}."
LOG_CLEAN_PER_FILE_REMOVE_FAILED_SUMMARY = "[CLEAN] Не удалось удалить симлинков модов: {count}."
LOG_CLEAN_PER_FOLDER_LINKS_REMOVED = "[PER-FOLDER] Отвязано модов: {count}."
LOG_CLEAN_PER_FOLDER_REMOVE_FAILED_SUMMARY = "[CLEAN] Не удалось удалить ссылок папок модов: {count}."
LOG_CLEAN_ERRORS_OMITTED = "[CLEAN] ...и еще ошибок: {count}."
LOG_CLEAN_CONTENT_LINKS_REMOVE_FAILED = "[CLEAN] Не удалось удалить ссылки контент-модов: {error}"
LOG_CLEAN_PROFILE_LINKS_REMOVED_SUMMARY = "[CLEAN] Удалено существующих ссылок для профиля '{profile_name}': {count}."

# Всплывающее окно опций очистки
DLG_TITLE_CLEAN_OPTIONS = "Параметры очистки"
CLEAN_OPTIONS_PROMPT = "Выберите одну или несколько опций:"
CLEAN_OPTION_STALE_ENTRIES = "Удалить устаревшие записи из mods_list.json."
CLEAN_OPTION_BROWSER_HISTORY = "Удалить локальную историю загрузок браузера CZT."
CLEAN_OPTION_CRASH_LOGS = "Удалить логи мониторинга сбоев."
CLEAN_OPTION_SYMLINKS = "Удалить существующие симлинки текущего профиля."
CLEAN_OPTIONS_APPLY = "Применить"
CLEAN_OPTIONS_CANCEL = "Отмена"

# Окно первоначальной настройки
LBL_FTS_CREATE_ROOT = "Создать корень"
LBL_FTS_INSTALL_UNRAR = "Установить UnRAR"
LBL_FTS_NEXUS_API_KEY = "Nexus API Key"
LBL_FTS_SAVE_KEY = "Сохранить ключ"
LBL_FTS_SET_PATH = "Задать путь"
LBL_FTS_OPEN_ROOT = "Открыть корень"

TIP_CREATE_ROOT = (
    "Нажмите 'Create Root', затем выберите предпочитаемый диск.\n"
    "CZT автоматически создаст корневые папки и задаст путь источника."
)
TIP_INSTALL_UNRAR = (
    "Скачайте и установите UnRAR.exe для распаковки модов.\n"
    "Устанавливайте в > Drive Selected For CZT Root/CZT Mod Manager/czt_tools/UnRAR.exe \n"
    "Примечание: после установки unrar можно нажать снова для автоопределения пути."
)
TIP_BROWSE_UNRAR = "Выберите путь к WinRAR.exe или UnRAR.exe, если уже установлено."
TIP_NEXUS_API = (
    "Получите свой API-ключ Nexus Mods\n"
    "Откроется сайт nexus\n"
    "Прокрутите страницу вниз, чтобы увидеть ключ"
)
MSG_API_KEY_SAVED_TITLE = "API-ключ сохранен"
MSG_API_KEY_SAVED_TEXT = "Nexus API-ключ сохранен в конфиг."

# Всплывающее окно пользовательских настроек

SETTINGS_RESET_BUTTON_TEXT = "Сброс"
SETTINGS_FONT_BUTTON_VALUE_TEXT = "{label}: {value}"

# Переопределения текста UI - сопоставление objectName виджета с отображаемым текстом
SETTINGS_UI_TEXT = {
    # Заголовки групп
    "General_Settings": "Общие настройки",
    "groupBox": "Расширенные настройки",
    "startupGroup_2": "Параметры цвета",
    "startupGroup_3": "Параметры шрифта",
    # Подписи кнопок цвета
    "groupBoxBorderColorBtn": "Цвет границы log box",
    "logBoxBackgroundColorBtn": "Цвет фона log box",
    "storageOverviewBorderColorBtn": "Граница обзора CZT",
    "lineSeparatorColorBtn": "Цвет разделительной линии",
    "selectedModBorderColorBtn": "Цвет границы выбранного мода",
    "entryBorderColorBtn": "Цвет границы записи",
    "entrySelectedBorderColorBtn": "Граница выбранной записи",
    "entryBorderHoverColorBtn": "Наведение границы записи",
    "entryBackgroundColorBtn": "Цвет фона записи",
    "descriptionBackgroundColorBtn": "Фон описания",
    "descriptionBorderColorBtn": "Граница описания",
    "installListBorderColorBtn": "Граница списка установки",
    "scrollbarHandleBgBtn": "BG ползунка scrollbar",
    "scrollbarHandleHoverBgBtn": "BG наведения ползунка scrollbar",
    "scrollbarBorderBtn": "Граница ползунка scrollbar",
    "tabBgColorBtn": "Цвет фона вкладки",
    "tabHoverBgBtn": "Фон наведения вкладки",
    "tabSelectedBgBtn": "Фон выбранной вкладки",
    "tabTextColorBtn": "Цвет текста вкладки",
    "tabHoverTextBtn": "Цвет текста наведения вкладки",
    "tabSelectedTextColorBtn": "Цвет текста выбранной вкладки",
    "customTabBorderColorBtn": "Цвет границы окна",
    "modListBorderColorBtn": "Цвет границы списка модов",
    "progressBarColorBtn": "Цвет полосы прогресса",
    "customColorLogBoxTextBtn": "Цвет текста log box",
    "dropdownDisplayColorBtn": "Основной цвет dropdown",
    "dropdownHoverColorBtn": "Цвет наведения dropdown",
    "dropdownBorderColorBtn": "Цвет границы dropdown",
    "dropdownBorderHoverColorBtn": "Наведение границы dropdown",
    "mainMenuVerticalBtnDisplayColorBtn": "Цвет вертикальной кнопки главного меню",
    "mainMenuVerticalBtnHoverColorBtn": "Наведение вертикальной кнопки главного меню",
    "mainMenuVerticalBtnBorderColorBtn": "Граница вертикальной кнопки главного меню",
    "mainMenuVerticalBtnBorderHoverColorBtn": "Наведение границы вертикальной кнопки главного меню",
    "mainMenuHorizontalBtnDisplayColorBtn": "Цвет кнопки ряда главного меню",
    "mainMenuHorizontalBtnHoverColorBtn": "Наведение кнопки ряда главного меню",
    "mainMenuHorizontalBtnBorderColorBtn": "Граница кнопки ряда главного меню",
    "mainMenuHorizontalBtnBorderHoverColorBtn": "Наведение границы кнопки ряда главного меню",
    "manageTopBtnDisplayColorBtn": "Цвет верхней кнопки Manage",
    "manageTopBtnHoverColorBtn": "Наведение верхней кнопки Manage",
    "manageTopBtnBorderColorBtn": "Граница верхней кнопки Manage",
    "manageTopBtnBorderHoverColorBtn": "Наведение границы верхней кнопки Manage",
    "deleteBtnDisplayColorBtn": "Цвет кнопки Delete",
    "deleteBtnHoverColorBtn": "Наведение кнопки Delete",
    "deleteBtnBorderColorBtn": "Граница кнопки Delete",
    "deleteBtnBorderHoverColorBtn": "Наведение границы кнопки Delete",
    "deleteBtnTextColorBtn": "Цвет текста кнопки Delete",
    "deleteBtnTextHoverColorBtn": "Наведение текста кнопки Delete",
    "saveBtnDisplayColorBtn": "Цвет кнопки Save",
    "saveBtnHoverColorBtn": "Наведение кнопки Save",
    "saveBtnBorderColorBtn": "Граница кнопки Save",
    "saveBtnBorderHoverColorBtn": "Наведение границы кнопки Save",
    "saveBtnTextColorBtn": "Цвет текста кнопки Save",
    "saveBtnTextHoverColorBtn": "Наведение текста кнопки Save",
    "actionBtnDisplayColorBtn": "Цвет кнопки действия",
    "actionBtnHoverColorBtn": "Наведение кнопки действия",
    "actionBtnBorderColorBtn": "Граница кнопки действия",
    "actionBtnBorderHoverColorBtn": "Наведение границы кнопки действия",
    "actionBtnTextColorBtn": "Цвет текста кнопки действия",
    "actionBtnTextHoverColorBtn": "Наведение текста кнопки действия",
    "okBtnDisplayColorBtn": "Цвет кнопки OK",
    "okBtnHoverColorBtn": "Наведение кнопки OK",
    "okBtnBorderColorBtn": "Граница кнопки OK",
    "okBtnBorderHoverColorBtn": "Наведение границы кнопки OK",
    "okBtnTextColorBtn": "Цвет текста кнопки OK",
    "okBtnTextHoverColorBtn": "Наведение текста кнопки OK",
    "cancelBtnDisplayColorBtn": "Цвет кнопки Cancel",
    "cancelBtnHoverColorBtn": "Наведение кнопки Cancel",
    "cancelBtnBorderColorBtn": "Граница кнопки Cancel",
    "cancelBtnBorderHoverColorBtn": "Наведение границы кнопки Cancel",
    "cancelBtnTextColorBtn": "Цвет текста кнопки Cancel",
    "cancelBtnTextHoverColorBtn": "Наведение текста кнопки Cancel",
    "launchGameBtnDisplayColorBtn": "Цвет кнопки Launch Game",
    "launchGameBtnHoverColorBtn": "Наведение кнопки Launch Game",
    "launchGameBtnBorderColorBtn": "Граница кнопки Launch Game",
    "launchGameBtnBorderHoverColorBtn": "Наведение границы кнопки Launch Game",
    "launchGameBtnTextColorBtn": "Цвет текста кнопки Launch Game",
    "launchGameBtnTextHoverColorBtn": "Наведение текста кнопки Launch Game",
    "miscBtnTextColorBtn": "Цвет текста misc-кнопки",
    "miscBtnTextHoverColorBtn": "Цвет текста misc-кнопки при наведении",
    "miscBtnColorDisplayBtn": "Основной цвет misc-кнопки",
    "miscBtnColorHoverBtn": "Цвет наведения misc-кнопки",
    "miscBtnColorBorderBtn": "Цвет границы misc-кнопки",
    "miscBtnBorderHoverColorBtn": "Наведение границы misc-кнопки",
    # Подписи кнопок шрифта
    "customFontHeaderIBtn": "Шрифт вкладок",
    "customFontHeaderMBtn": "Шрифт меток",
    "customFontLogBoxBtn": "Шрифт log box",
    "customFontLabelsBtn": "Шрифт списка модов",
    "customFontTooltipBtn": "Шрифт tooltip",
    "customFontCbBtn": "Шрифт checkbox",
    "customFontButtonBtn": "Шрифт кнопок",
    "customFontMainMenuVerticalButtonsBtn": "Шрифт левых кнопок главного меню",
    "customFontMainMenuTopButtonsBtn": "Шрифт верхних кнопок главного меню",
    "customFontManageTabButtonsBtn": "Шрифт кнопок вкладки Manage",
    # Общие подписи / чекбоксы
    "generalUseDownloadsAsSourceCheckBox": "Использовать папку downloads как источник.",
    "generalUseModsSourceAsSourceCheckBox": "Использовать папку mod_staging как источник.",
    "generalUseBuiltInNexusBrowserCheckBox": "Открывать ссылки модов во встроенном браузере CZT.",
    "generalRegisterNxmHandlerCheckBox": "Назначить обработчиком кнопки 'Mod Manager Download'.",
    "generalUpdateOnlyEnabledModsCheckBox": "Проверять обновления только для включенных модов при сканировании.",
    "generalDownloadModsAfterScanCheckBox": "Автоматически скачивать моды с пометкой 'доступно обновление'.",
    "generalDeleteAfterInstalledCheckBox": "Автоматически удалять архивы источника после установки мода.",
    "generalProtectEnabledModsFromDeletionCheckBox": "Защищать включенные моды от удаления.",
    "manageHomeCheckBox": "Сделать вкладку 'Manage' домашней.",
    "installHomeCheckBox": "Сделать вкладку 'Main Menu' домашней.",
    "enableCztBetaAlertsCheckBox": "Включить оповещения о бета-релизах CZT.",
    "scanUpdatesOnStartupCheckBox": "Проверять моды на обновления при запуске.",
    "updateScanCacheHoursLabel": "Частота сканирования при запуске (ч):",
    "musicLabel": "Трек:",
    "menuMusicVolumeLabel": "Громкость:",
    "menuMusicCheckBox": "Включить музыку меню.",
    "pauseMenuMusicAfterLaunchCheckBox": "Останавливать музыку меню после запуска игры.",
    "buttonHoverCheckBox": "Включить звук наведения кнопок.",
    "buttonClickCheckBox": "Включить звук клика кнопок.",
    "languageLabel": "Язык:",
    # Расширенные подписи / чекбоксы
    "downloadParallelWorkersLabel": "Максимум одновременных загрузок:",
    "backgroundThreadsLabel": "Максимум фоновых потоков:",
    "installLiveLogThresholdLabel": "Порог живого лога прогресса (MB):",
    "installCacheSessionCheckBox": "Кэшировать выбор файлов (только на сессию).",
    "installCachePersistentCheckBox": "Кэшировать выбор файлов (постоянно).",
    "installCacheAutoClearCheckBox": "Автоочистка постоянного локального кэш-файла.",
    "installCacheMaxSizeLabel": "Порог автоочистки (KB):",
    "similarityPrimaryTokensLabel": "Минимальное первичное совпадение токенов:",
    "similarityPrimaryRatioLabel": "Коэффициент первичного совпадения:",
    "generalEnableSecondaryInstallSafetyCheckBox": "Включить вторичную защиту установки.",
    "similaritySecondaryTokensLabel": "Минимальное вторичное совпадение токенов:",
    "similaritySecondaryRatioLabel": "Коэффициент вторичного совпадения:",
    "saveButton": "Сохранить",
}

SETTINGS_HELP_TEXT = (
    "Параметры ниже определяют, насколько строго CZT ищет возможные файлы-замены во время установки. "
    "Авторы модов часто слегка переименовывают файлы между версиями, поэтому CZT сравнивает входящие файлы с уже "
    "установленными и предлагает выбор, когда находит вероятное совпадение.\n"
    "Точные совпадения имен файлов заменяются автоматически. Параметры ниже используются только для близких совпадений, "
    "когда имена различаются, но выглядят связанными.\n\n"
    "Совпадение токенов - это сколько частей имени файла должно совпасть, чтобы файл считался кандидатом.\n"
    "Коэффициент управляет строгостью: более низкие значения показывают больше кандидатов (шире, но менее точно), "
    "более высокие - меньше (точнее, но могут пропустить валидные обновления, если поставить слишком высоко).\n\n"
    "Вторичная защита опциональна и работает как более широкий резервный фильтр для крайних случаев, которые может пропустить первичная проверка."
)

TIP_REGISTER_NXM_HANDLER = (
    "Когда включено, нажатие кнопки 'Mod Manager Download' на странице мода приводит к\n"
    "прямой отправке файла в CZT для загрузки и установки. Все метаданные мода сохраняются в момент установки.\n"
    "- Работает для всех типов аккаунтов Nexus (free и premium).\n"
    "НЕ ОТКЛЮЧАЙТЕ, ЕСЛИ ТОЛЬКО НЕ СТОЛКНУЛИСЬ С ПРОБЛЕМАМИ, КОГДА CZT ПЕРЕХВАТЫВАЕТ ДРУГИЕ МЕНЕДЖЕРЫ ПРИ ЗАГРУЗКЕ."
)

TIP_OPEN_IN_APP_BROWSER = (
    "Когда включено, кнопка обзора, изображения модов и иконка ссылки открывают Nexus во встроенном браузере CZT.\n"
    "Когда выключено, все ссылки открываются во внешнем браузере по умолчанию."
)

TIP_INSTALL_LIVE_LOG_THRESHOLD = (
    "Минимальный размер установки, после которого CZT показывает живой прогресс установки в лог-окне.\n"
    "Полезно для крупных файлов, когда иначе приложение выглядит как будто ничего не происходит."
)

TIP_DOWNLOAD_PARALLEL_WORKERS = (
    "Максимальное число загрузок, которые CZT может выполнять параллельно.\n"
    "⚠️ Более высокие значения ускоряют пакетные загрузки, но могут вызывать нестабильность."
)

TIP_BACKGROUND_THREADS = (
    "Лимит фоновых потоков.\n"
    "На этот параметр влияют операции Update Scan/Loadout/Install.\n"
    "Более высокие значения позволяют запускать больше задач одновременно.\n"
    "⚠️ Более высокие значения могут ускорить действия, но вызвать нестабильность."
)

TIP_UPDATE_SCAN_CACHE_HOURS = (
    "- Если вы часто перезапускаете приложение и хотите избежать полного сканирования при старте, установите большее значение, например 6.\n"
    "- Если хотите выполнять полное сканирование при каждом запуске (или каждом нажатии проверки всех модов), установите 0.\n"
    "- НЕ ВЛИЯЕТ НА ЧАСТОТУ ИСПОЛЬЗОВАНИЯ ИНДИВИДУАЛЬНОЙ ПРОВЕРКИ ОБНОВЛЕНИЙ В ОКНЕ \"EDIT MOD ENTRY\"."
)

TIP_SAVE_SETTINGS = (
    "Сохранить настройки и применить изменения.\n"
    "> Примечание: некоторые настройки требуют перезапуска для полного применения."
)

# Подсказки кнопок сброса
TIP_RESET_LIVE_LOG_THRESHOLD = "Сбросить порог живого прогресса к значению по умолчанию."
TIP_RESET_DOWNLOAD_WORKERS = "Сбросить максимум одновременных загрузок к значению по умолчанию."
TIP_RESET_BACKGROUND_THREADS = "Сбросить максимум фоновых потоков к значению по умолчанию."
TIP_RESET_PRIMARY_TOKENS = "Сбросить первичное совпадение токенов к значению по умолчанию."
TIP_RESET_PRIMARY_RATIO = "Сбросить первичный коэффициент к значению по умолчанию."
TIP_RESET_SECONDARY_TOKENS = "Сбросить вторичное совпадение токенов к значению по умолчанию."
TIP_RESET_SECONDARY_RATIO = "Сбросить вторичный коэффициент к значению по умолчанию."

# Подсказки кэша установки
TIP_CACHE_SESSION = (
    "Сохранять выбор файла из знакомых архивов до закрытия CZT.\n"
    "Используйте кнопку обновления для очистки кэша текущей сессии."
)
TIP_CACHE_PERSISTENT = (
    "Сохранять выбор файла в файл, чтобы он оставался после перезапуска.\n"
    "Используйте кнопку обновления для очистки локального кэш-файла."
)
TIP_CACHE_AUTO_CLEAR = "При включении постоянный кэш автоматически очищается после превышения лимита ниже."
TIP_CACHE_MAX_SIZE = "Максимальный размер постоянного кэш-файла в KB перед автоочисткой."
TIP_CLEAR_SESSION_CACHE = "Очистить кэш выбора файлов текущей сессии."
TIP_CLEAR_PERSISTENT_CACHE = "Очистить постоянный кэш выбора файлов."
TIP_RESET_CACHE_SIZE_LIMIT = "Сбросить лимит размера постоянного кэша к значению по умолчанию."

# Резервный трек музыки
DEFAULT_MUSIC_TRACK = "По умолчанию"

# Выпадающий список языка
LBL_LANGUAGE = "Язык:"
TIP_LANGUAGE_DROPDOWN = (
    "Выберите язык интерфейса для CZT Mod Manager.\n"
    "Дополнительные языковые пакеты можно добавить в корневую папку > CZT Mod Manager/plugins/language_packs/.\n"
    "Изменения вступят в силу после перезапуска приложения."
)
MSG_LANGUAGE_RESTART = "Язык изменен. Перезапустите CZT Mod Manager, чтобы изменения применились полностью."

TIP_MENU_MUSIC_DROPDOWN = (
    "Выберите фоновый трек для меню.\n"
    "Вы можете добавить свои треки, поместив их в корневую папку > CZT Mod Manager/plugins/audio/menu_music.\n"
    "Поддерживаемые форматы: .mp3, .wav, .ogg"
)
TIP_BETA_ALERTS_RESET = "Сбросить скрытые бета-уведомления, чтобы при запуске снова показывался последний бета-промпт."
TIP_INSTALL_CACHE_MAX_RESET = "Сбросить лимит размера постоянного кэша к значению по умолчанию."
MSG_FONT_BLOCKED_TITLE = "Шрифт заблокирован"
MSG_FONT_BLOCKED_TEXT = "Шрифт '{font_family}' не разрешен. Выберите другой шрифт."
MSG_SETTINGS_SAVED_TITLE = "Настройки сохранены"
MSG_SETTINGS_SAVED_CHANGED = "Были изменены следующие настройки:"
MSG_SETTINGS_SAVED_NO_CHANGES = "Настройки не изменялись."

# строки log/status для controls.py
LOG_CONFIG_NOT_SAVED_NO_ROOT = "❌ [ERROR] Конфиг не сохранен: czt_root_folder не задан!\n    > Перейдите во вкладку USER SETTINGS и нажмите 'CREATE ROOT'"
DEFAULT_SET_PROFILE_PATH = "Не задано. Если используете ручную настройку путей, нажмите [Set Install] и [Set EXE]"
DEFAULT_STEAM_LIBRARY_PATH = "Не задано. Нажмите [Detect Steam]"
DEFAULT_CURRENT_PROFILE = "Не задано. Выберите корректный профиль."
DEFAULT_EXE_NOT_FOUND = "Не найдено, \n    Пользователи Steam: нажмите [Detect Steam], затем [Launch Game]\n     Ручной режим: нажмите [Set EXE] для исправления."
LOG_SAVE_CONFIG_SUMMARY = (
    "[SAVE CONFIG] Сохранено ✓\n"
    "[QUICK CFG SUMMARY]\n"
    "⇾ Текущий профиль: {current_profile}\n"
    "⇾ Режим пути: {profile_path_mode}\n"
    "⇾ Цель SymLink: {set_profile_path}\n"
    "⇾ Целевой EXE: {exe_path}"
)
LOG_AUTO_SAVE_NO_ROOT = "❌ [ERROR] czt_root_folder не задан. Конфиг не сохранен!"
LOG_BROWSE_NO_ROOT = "\n[ERROR] Корневая папка не задана! Нажмите 'CREATE ROOT', чтобы начать использовать CZT.\n"
LOG_PROFILE_MODS_FOLDER_NOT_FOUND = "[ERROR] Папка модов профиля не найдена: {profile_mods_path}"
LOG_DEST_FOLDER_NOT_FOUND = "[ERROR] Папка назначения не найдена."
LOG_OPENED_INSTALL_AND_MODS = "Открыты папка установки игры и папка Mods."
LOG_SELECTED_PROFILE = "[PROFILE] Выбран профиль: {current_profile}"
LOG_PROFILE_FOLDER_WARN = "[PROFILE][WARN] Не удалось гарантировать папки профиля для '{current_profile}': {error}"
