---
name: remotion
description: Creates programmatic videos using React and Remotion framework with real-time browser preview.
---

# Remotion Video Creator

Use this skill for creating or editing videos programmatically using React components and Remotion.

## Trigger phrases
- "Remotion", "create video", "animate video", "remotion-videos/", "remotion.config.ts", "React video"

## Prerequisites

```bash
npx create-video@latest   # Create Remotion project externally first
cd remotion-videos
npm run dev               # Start dev server for browser preview
```

## Core Concepts

- Videos are React components — every frame is a render
- `useCurrentFrame()` gives the current frame number
- `interpolate()` maps frame ranges to value ranges
- `spring()` creates physics-based animations
- `<Sequence>` offsets when a component starts playing
- `<Composition>` defines video dimensions, fps, and duration

## Fundamental Animation Pattern

```tsx
import { useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export const MyComp: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: 'clamp',
  });

  const scale = spring({ frame, fps, config: { damping: 200 } });

  return <div style={{ opacity, transform: `scale(${scale})` }}>Hello</div>;
};
```

## Key APIs

| API | Purpose |
|-----|---------|
| `useCurrentFrame()` | Current frame number |
| `useVideoConfig()` | fps, width, height, durationInFrames |
| `interpolate(frame, [in], [out])` | Map frames to values |
| `spring({ frame, fps, config })` | Physics spring animation |
| `<Sequence from={30}>` | Delay component start by 30 frames |
| `<Audio src={...} />` | Add audio |
| `<Video src={...} />` | Embed video |
| `<Img src={...} />` | Images (use instead of `<img>`) |

## Composition Definition

```tsx
// src/Root.tsx
import { Composition } from 'remotion';

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="MyVideo"
      component={MyComp}
      durationInFrames={150}
      fps={30}
      width={1920}
      height={1080}
    />
  </>
);
```

## Common Patterns

### Fade in text
```tsx
const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
```

### Slide in from left
```tsx
const x = interpolate(frame, [0, 20], [-100, 0], { extrapolateRight: 'clamp' });
```

### Staggered list items
```tsx
items.map((item, i) => {
  const delay = i * 10;
  const opacity = interpolate(frame, [delay, delay + 20], [0, 1], { extrapolateRight: 'clamp' });
  return <div style={{ opacity }}>{item}</div>;
});
```

## Rules

- Always use `<Img>` not `<img>` for images (Remotion handles asset loading)
- Always use `<Audio>` not `<audio>` for audio
- Keep components pure — same frame always renders same output
- Use `staticFile()` for local assets: `staticFile('logo.png')`
- Load fonts with `loadFont()` from `@remotion/google-fonts`

## Rules Folder

Detailed rules for specific topics are in `rules/`. Load only the relevant rule file when needed:
- `rules/animations.md` — easing, springs, interpolation
- `rules/media.md` — images, video, audio, GIFs, fonts
- `rules/captions.md` — SRT imports, transcription
- `rules/charts.md` — data visualization
- `rules/3d.md` — Three.js integration
- `rules/tailwind.md` — TailwindCSS setup
- `rules/compositions.md` — sequencing, trimming
