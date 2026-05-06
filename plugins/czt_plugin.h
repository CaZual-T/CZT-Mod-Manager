/*
 * CZT Native Plugin ABI v1
 * ------------------------
 * Public C header for native CZT plugins. Compile your plugin as a Windows DLL
 * exporting `czt_plugin_init` and `czt_plugin_shutdown`. Declare the DLL in
 * your plugin.json with:
 *
 *     "native_lib": "your_plugin.dll",
 *     "native_abi": 1
 *
 * The DLL is loaded by ctypes when the host plugin's register(host) calls
 *     host.native.load("your_plugin.dll", abi_version=1)
 *
 * All strings are UTF-8.
 */
#ifndef CZT_PLUGIN_H
#define CZT_PLUGIN_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define CZT_ABI_V1 1

/* --- Callback typedefs (provided by the host) ------------------------- */

/*
 * Log a message via the CZT log box (and stdout).
 * msg: NUL-terminated UTF-8 string.
 */
typedef void (*CztLogFn)(const char* msg);

/*
 * Emit an event onto the global event bus.
 * event_name:    NUL-terminated UTF-8 string (see plugins_.events.KNOWN_EVENTS).
 * json_payload:  NUL-terminated UTF-8 JSON object string. Pass NULL or "" for
 *                an empty payload. Must be a flat object whose keys become
 *                **kwargs for Python listeners.
 */
typedef void (*CztEmitFn)(const char* event_name, const char* json_payload);

/*
 * Look up a config value by key.
 * key:        NUL-terminated UTF-8 string (e.g. "czt_root_folder").
 * Returns:    NUL-terminated UTF-8 pointer owned by the host, valid until the
 *             next call to get_cfg_string with the same key. Returns NULL if
 *             the key is missing. Non-string config values are returned as
 *             their JSON encoding.
 */
typedef const char* (*CztGetCfgFn)(const char* key);

/* --- Host interface struct (passed to czt_plugin_init) ---------------- */

typedef struct {
    int            abi_version;       /* must equal CZT_ABI_V1 */
    const char*    plugin_id;         /* utf-8, NUL-terminated */
    const char*    czt_root;          /* utf-8, NUL-terminated */
    CztLogFn       log;
    CztEmitFn      emit_event;
    CztGetCfgFn    get_cfg_string;
} CztHostV1;

/* --- Required exports -------------------------------------------------- */

/*
 * Initialise the plugin.
 * Return 0 on success; any non-zero value aborts the load and the DLL is
 * unloaded without a follow-up shutdown call.
 *
 * The host pointer is valid only for the duration of this call. Copy any
 * fields and callback pointers you need to keep.
 */
__declspec(dllexport) int  czt_plugin_init(const CztHostV1* host);

/*
 * Cleanly shut down the plugin. Always called before the DLL is unloaded
 * (unless czt_plugin_init returned non-zero). After this returns, all
 * captured callbacks are no longer valid.
 */
__declspec(dllexport) void czt_plugin_shutdown(void);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* CZT_PLUGIN_H */
