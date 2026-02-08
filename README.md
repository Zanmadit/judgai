# judgai

AI Hackathon Judge is an autonomous system that evaluates hackathon projects the way a real jury would — by analyzing the GitHub repository, demo video, and project claims together.

Instead of relying only on a README or a short demo, the system explores the codebase, verifies claims, and produces structured scores and detailed jury-style feedback.

## What It Does

**Given**:
- a GitHub repository link
- a demo video
- a team name
**The system automatically**:
1. Reads and analyzes the README to extract project claims
2. Explores the GitHub repository and selects priority files relevant to those claims
3. Analyzes the selected source code
4. Processes the demo video (frames + audio) to understand actual behavior
5. Produces a structured verdict with scores and detailed feedback


## Evaluation Criteria

- Novelty – how original and innovative the idea is
- Technical execution – code quality, architecture, and implementation
- Practical usefulness – real-world applicability and value

The output also includes strict jury-style feedback, highlighting strengths and areas for improvement.

---

## Tech Stack

**Backend**: FastAPI, Python
**LLM**: Gemini API
**GitHub integration**: PyGithub
**Video processing**: OpenCV, FFmpeg
**Frontend**: HTML, CSS, JavaScript
**Output format**: JSON + Markdown


## Future Improvements

- Claim → code line evidence mapping
- Audio transcription and NLP analysis of demos
- PDF / document analysis
- Scoring confidence estimation
- Web dashboard with comparison between teams


## Use Cases

1. Hackathons and coding competitions
2. Internal company demos and reviews
3. Educational project evaluation
4. Pre-screening projects before final judging