declare module '@tauri-apps/plugin-updater' {
  export function check(): Promise<{ version: string; download: () => Promise<void>; install: () => Promise<void> } | null>;
}
