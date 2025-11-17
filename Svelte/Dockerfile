# Stage 1 — Build
FROM node:20-alpine AS builder

WORKDIR /app

# Enable pnpm
RUN corepack enable

# Copy lockfile and package info
COPY package.json pnpm-lock.* ./

# Install dependencies
RUN pnpm install

# Copy rest of project
COPY . .

# Build SvelteKit
RUN pnpm build


# Stage 2 — Run (production)
FROM node:20-alpine AS runner

WORKDIR /app

# Copy production build + node_modules from builder
COPY --from=builder /app/build ./build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000
ENV NODE_ENV=production

CMD ["node", "build"]