# Azure Face API Demo — Detection, Emotion, and the Art of Letting Go

This repository documents my attempt to run Azure's Face API using Python and the legacy SDK (`azure-cognitiveservices-vision-face`). The goal was to detect faces and extract age, gender, and emotion attributes from local images.

Despite correct credentials, valid image formats, and multiple debugging attempts, the API consistently returned `(InvalidRequest)` errors. This README captures the journey, the scripts, and the decision to pivot.

---

## Setup

- Python 3.11
- Installed packages:
  - `azure-cognitiveservices-vision-face`
  - `msrest`
- Azure Face API resource deployed in Southeast Asia
- Authentication via `CognitiveServicesCredentials` using Face API Key

---

## Scripts

### `faceapidemo.py`
Final version with all recommended fixes:
- Explicit `return_face_id=False`
- Detection model set to `'detection_03'`
- Recognition model added (`'recognition_04'`)
- Image stream diagnostics included

Outcome: `(InvalidRequest)` persisted.

### `facetrial.py`
Initial version testing image loop and CSV logging. Helped confirm stream behavior and attribute extraction logic.

### `facescript.py`
Variant exploring credential methods (`AzureCliCredential`) and alternate detection models. Used for isolating SDK quirks.

---

## Troubleshooting Attempts

- Verified image format and stream
- Tried multiple detection models (`detection_01`, `detection_03`)
- Added `recognition_model` and disabled `faceId`
- Confirmed endpoint and key
- Ran diagnostics and printed stream previews
- Switched between credential types

---

## Outcome

All requests returned:


This may be due to:
- SDK limitations
- Region-specific restrictions
- Responsible AI policy changes
- Deprecated or restricted features (e.g., `faceId` inference)

---

## Next Steps

- Pivot to REST API for more control and transparency
- Explore `azure-ai-vision` SDK for updated workflows
- Document this trial as part of my developer journey

---

## Reflection

This wasn’t a failure; it was a deep dive into Azure’s quirks, SDK behavior, and the importance of graceful exits. I’m proud of the work, the resilience, and the clarity it gave me.

Sometimes the best demo is the one that teaches you when to pivot.

---

## Personal Note


Teddy watched me debug this with quiet loyalty. I built this script not just for technical mastery, but for sanctuary, for the day I can run code without outages, without fear, and with full creative freedom.
I kept pushing through, even after repairing my system three times due to malware. Each time I rebuilt the environment, reinstalled the SDKs, and restructured the script, I hoped this would be the run that worked. But even after all that effort, the API still didn’t push through.

*Écrit sous des lumières vacillantes, avec Teddy à mes côtés. Août 2025, Iloilo.*
*Je pivote, mais je ne tombe pas. Je construirai encore, avec grâce et feu.*
