import { goto } from '$app/navigation';
import { browser } from '$app/environment';

// Global click handler for buttons with href
if (browser) {
	// Wait for DOM to be ready
	const setupGlobalNavigation = () => {
		document.addEventListener('click', (e) => {
			const target = e.target as HTMLElement;
			
			// Check if clicked element is a button with href, or is inside one
			const button = target.closest('button[href]') as HTMLButtonElement;
			
			if (button) {
				e.preventDefault();
				const href = button.getAttribute('href');
				if (href) {
					goto(href);
				}
			}
		}, true); // Use capture phase to ensure we get it before other handlers
	};
	
	// Set up immediately if document is ready, otherwise wait
	if (document.readyState !== 'loading') {
		setupGlobalNavigation();
	} else {
		document.addEventListener('DOMContentLoaded', setupGlobalNavigation);
	}
}
