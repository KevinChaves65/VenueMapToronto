import { writable } from 'svelte/store';

export const sidebarOpen = writable(true);

export function toggleSidebar() {
  sidebarOpen.update((v) => !v);
}
export function closeSidebar() {
  sidebarOpen.set(false);
}
export function openSidebar() {
  sidebarOpen.set(true);
}
