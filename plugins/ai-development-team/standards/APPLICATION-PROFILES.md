# Application profiles — select at project intake

| Profile | Typical interface | Trusted core | Data/persistence | Delivery/operations focus |
| --- | --- | --- | --- | --- |
| Desktop/native | Qt/PySide/WPF/WinUI/Avalonia/Electron | Local application module or remote service | SQLite/files or service backend | Installer, OS support, offline data, upgrade/migration |
| Web | SPA/server-rendered | API/server, domain services | SQL/NoSQL as selected | Browser matrix, separate frontend builds, server deployment |
| Python web | Django/Flask/FastAPI | Python services/tasks | ORM/repositories/migrations | Virtual env, Python deps, ASGI/WSGI, jobs, migrations |
| Hybrid | Desktop/mobile + web API | Local and remote components | Local cache + remote store | Sync/conflict, versioning, installers, network failure |
| Mobile | iOS/Android/cross-platform | On-device and remote | Secure local stores + backend | Signing, app store/release, offline sync |
| CLI/embedded | Terminal/device interface | Local services/modules | Local files/SQL/remote backend | Device limits, packages, hardware/recovery |

The same **ten agents** operate for all these types. Do not confuse module-level ownership with independent deployment. Decide based on requirements, chosen runtime and version compatibility, not because an agent name exists.
