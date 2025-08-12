# Carlos Arroyo Portfolio

A modern, dark-themed portfolio website inspired by the Nikola Tesla portfolio template. Built with Astro, React, and TailwindCSS.

## Features

- 🎨 **Modern Dark Theme** - Sophisticated dark design with purple and blue gradients
- ✨ **Smooth Animations** - Framer Motion powered animations and transitions
- 📱 **Responsive Design** - Optimized for all devices and screen sizes
- ⚡ **Fast Performance** - Built with Astro for optimal loading speeds
- 🎯 **Interactive Elements** - Hover effects and micro-interactions
- 🌟 **Glass Morphism** - Modern UI with backdrop blur effects

## Tech Stack

- **Framework**: Astro 5.12.9
- **UI Library**: React 19
- **Styling**: TailwindCSS 4
- **Animations**: Framer Motion
- **Language**: TypeScript

## Prerequisites

Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (version 18 or higher)
- [npm](https://www.npmjs.com/) or [pnpm](https://pnpm.io/) or [yarn](https://yarnpkg.com/)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio-project
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   pnpm install
   # or
   yarn install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   # or
   pnpm dev
   # or
   yarn dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:4321` to see your portfolio

## Project Structure

```
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   └── HeroSection.tsx      # Animated hero section
│   ├── layouts/
│   │   └── Layout.astro         # Main layout with dark theme
│   ├── pages/
│   │   ├── index.astro          # Homepage
│   │   ├── about.astro          # About page
│   │   ├── projects.astro       # Projects page
│   │   ├── bi.astro            # Business Intelligence page
│   │   ├── code.astro          # Code samples page
│   │   └── contact.astro       # Contact page
│   └── styles/
│       └── global.css          # Global styles and animations
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

## Customization

### Colors and Theme
The portfolio uses a dark theme with purple and blue gradients. You can customize the colors by modifying:
- `src/layouts/Layout.astro` - Main layout colors
- `src/styles/global.css` - Custom CSS variables and animations
- `src/components/HeroSection.tsx` - Hero section styling

### Content
Update the content in:
- `src/pages/index.astro` - Homepage content
- `src/layouts/Layout.astro` - Navigation and footer links
- Individual page files for specific content

### Animations
Customize animations in:
- `src/components/HeroSection.tsx` - Hero animations
- `src/styles/global.css` - CSS animations
- Use Framer Motion for React component animations

## Build and Deploy

1. **Build for production**
   ```bash
   npm run build
   ```

2. **Preview the build**
   ```bash
   npm run preview
   ```

3. **Deploy**
   The site is configured for deployment on Vercel, but can be deployed to any hosting service.

## Design Inspiration

This portfolio is inspired by the [Nikola Tesla Portfolio Template](https://github.com/iann-mathaiya/nikola-tesla) by Iann Mathaiya, featuring:
- Dark, sophisticated color scheme
- Smooth animations and transitions
- Modern glass morphism effects
- Gradient text and backgrounds
- Interactive hover states

## License

This project is licensed under the MIT License.

## Contact

Carlos Arroyo - [LinkedIn](https://www.linkedin.com/) - [GitHub](https://github.com/)
