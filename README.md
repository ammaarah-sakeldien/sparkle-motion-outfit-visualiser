# Sparkle Motion: A personalised Outfit Visualiser

A Flask web app that fits clothing images into a full-body illustrated "doll" using OpenCV. The doll and the clothing are hand-drawn in a single art style by an illustrator collaborator, so every outfit looks cohesive instead of warped or pasted togther.

>**Status:** Still a work in progress. The artwork is not included in this repository, so the app won't run until you add your own images

## The Problem
It's hard to picture how individual pieces will look together, and inspiration boards like Pinterest show outfits made of items you don't own. This app lets people experiment with outfits on a figure that represents themselves.

## How It Works
1. Each garment is a PNG with a transparent background, and each has anchor points that mark where it attaches to the doll.
2. The app resizes each garment so its anchor points line up with the matching points on the doll.
3. OpenCV blends the garment onto the doll using its transparency, and layers are stacked in order, for example, bottoms before tops.
4. The FLask app serves the finished, dressed doll image to the browser.

## Features
**Working so far**
* Fitting garment images onto the doll by matching anchor points
* Transparency blending with OpenCV
* A Flask web app that serves the dressed doll image
* A helper tool for finding anchor coordinates

**Planned**
* **App closet:** a library of hand-drawn clothing items, such as tops, bottoms, shoes, etc., that users can mix and match.
* **Styling options:** toggleable variants such as tucked-in tops or cinched waists, a common styling technique that similar apps rarely support.
* **Users closet:** users add clothes they actually own, represented in the app's art style so they match the doll
* **Database:** SQLite storage for garments, categories, and layer data, with garments marked as app closet or user closet items
* **Accounts and saved outfits**

## Project Files
**File & Their Purpose**

- `app.py` -> Flask web app that serves the dressed doll image.
- `imageWarpingV1.py` -> Standalone version that open the result in a window
- `keypoints.py` -> Helper to click on an image and print anchor coordinates

## Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Image processing | OpenCV |
| Frontend | HTML, CSS, JavaScript |
| Database (planned) | SQLite |

## Artwork Requirements

The artwork is not included, so you need to supply your own:
- `doll.png`: the base doll image
- Garment PNGs with transparent backgrounds

Use `keypoints.py` to click on the doll and on each garment and print the anchor coordinates, then use those coordinates in the app.

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Security Considerations (Upload Phase)

Handling user-submitted files will require:
- Validating file types and sizes
- Sanitising filenames
- Storing files safely
- Ensuring one user cant access another users files

## Collaboration

The artwork is drawn by a friend, making this a collaboration between development and illustration.

## Roadmap
- [x] Garment fitting with anchor points and transparency blending
- [x] Flask app serving the dressed doll
- [ ] App closet with hand drawn garments
- [ ] Tucked and cinched styling variants
- [ ] User accounts and saved outfits
- [ ] User closet with secure uploads
