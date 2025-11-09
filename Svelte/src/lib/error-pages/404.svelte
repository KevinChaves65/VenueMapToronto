<div class="error-404-container">
	<div class="content">
		<!-- 404 Number -->
		<h1 class="error-code">
			404
		</h1>
		
		<!-- Error Message -->
		<div class="error-message">
			<h2 class="message-title">
				Page Not Found
			</h2>
			<p class="message-description">
				The page you're looking for doesn't exist or has been moved.
				<br />
				Let's get you back on track.
			</p>
		</div>
		
		<!-- Action Buttons -->
		<div class="action-buttons">
			<button 
				class="btn-primary"
				href="/"
			>
				<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
				</svg>
				Return Home
			</button>
			
			<button 
				class="btn-secondary"
				onclick={() => window.history.back()}
			>
				<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<path d="M15 19l-7-7 7-7"/>
				</svg>
				Go Back
			</button>
		</div>
	</div>
</div>

<style>
	.error-404-container {
		min-height: calc(100vh - 200px);
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: var(--color-tertiary-darker);
		padding: 2rem;
	}
	
	.content {
		text-align: center;
		max-width: 600px;
	}
	
	/* 404 Number */
	.error-code {
		font-size: clamp(80px, 15vw, 150px);
		font-weight: 900;
		color: var(--color-primary);
		margin: 0 0 1rem 0;
		letter-spacing: -5px;
		line-height: 1;
	}
	
	/* Message */
	.error-message {
		margin-bottom: 3rem;
	}
	
	.message-title {
		font-size: 2rem;
		font-weight: 700;
		color: var(--color-secondary);
		margin-bottom: 1rem;
	}
	
	.message-description {
		font-size: 1.1rem;
		color: var(--color-tertiary-lighter);
		line-height: 1.6;
	}
	
	/* Buttons */
	.action-buttons {
		display: flex;
		gap: 1rem;
		justify-content: center;
		flex-wrap: wrap;
	}
	
	.btn-primary,
	.btn-secondary {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		padding: 0.875rem 2rem;
		border: none;
		border-radius: 8px;
		font-size: 1rem;
		font-weight: 600;
		cursor: pointer;
		transition: all 0.2s ease;
	}
	
	.btn-primary {
		background-color: var(--color-primary);
		color: white;
	}
	
	.btn-primary:hover {
		background-color: var(--color-primary-dark);
		transform: translateY(-1px);
	}
	
	.btn-secondary {
		background-color: transparent;
		color: var(--color-secondary);
		border: 2px solid var(--color-secondary-dark);
	}
	
	.btn-secondary:hover {
		background-color: var(--color-secondary-dark);
		color: var(--color-tertiary);
		border-color: var(--color-secondary-dark);
	}
	
	.btn-primary svg,
	.btn-secondary svg {
		flex-shrink: 0;
	}
</style>