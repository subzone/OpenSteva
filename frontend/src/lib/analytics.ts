/**
 * Frontend analytics client — disabled for OpenSteva.
 *
 * All external telemetry is disabled. These functions are no-ops
 * that maintain the same interface so callers don't need changes.
 */

export async function initAnalytics(): Promise<void> {}
export function track(_event: string, _properties: Record<string, unknown> = {}): void {}
export function flush(): void {}
export function isAnalyticsEnabled(): boolean { return false; }
export function getAnonId(): string { return ''; }
export async function hashId(_s: string): Promise<string> { return ''; }
export function detectPlatform(): string { return 'web'; }
