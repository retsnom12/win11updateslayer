# Windows 11 Update Slayer 

**Windows 11 Update Slayer** is a lightweight, aggressive system optimization and automation utility designed to completely freeze, disable, and prevent forced Windows 11 updates, telemetry, and background resource-heavy update services. It grants power-users, developers, and system administrators absolute control over their operating system environment.

---

## 🚀 Key Features

* **Complete Update Suppression:** Force-stops and disables core Windows Update services including `wuauserv`, `bits`, `dosvc`, and `UsoSvc`.
* **Registry & Group Policy Enforcement:** Hardens the system against automatic re-enabling triggers by modifying crucial Windows Registry keys and system policies.
* **Telemetry & Bloatware Mitigation:** Blocks intrusive background data transmission related to update delivery optimization and Microsoft telemetry.
* **One-Click Execution:** Lightweight architecture designed for rapid, seamless system optimization without leaving persistent memory footprints.
* **Persistent Protection:** Designed to counter Windows' built-in self-healing mechanisms that typically turn update services back on automatically.

---

## 🛠️ Technical Overview & Architecture

The script operates directly at the Windows core configuration layer, handling system-level administrative tasks:

1. **Service Interruption:** Gracefully terminates running update loops and modifies service startup types to `Disabled`.
2. **Access Control Hardening:** Restricts system permissions on critical update executables to prevent automatic re-triggering by the OS.
3. **Task Scheduler Cleanup:** Disables hidden built-in scheduled tasks that Microsoft uses to force updates and reboots during active hours.

---

## 📂 Project Structure

```text
├── win11updateslayer.bat / .ps1  # Core automation script (Batch/PowerShell optimized)
├── assets/                       # Documentation or optional configuration tweaks
└── README.md                     # Technical documentation
