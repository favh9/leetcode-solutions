# LeetCode Solutions API

My LeetCode journey following the [NeetCode 150](https://neetcode.io/practice) study plan - with a twist. Each solution is exposed as an **API endpoint** using **FastAPI**, combining algorithm practice with API development.

I follow the NeetCode 150 since it's topic-based and pattern-organized, and then I solve the LeetCode problems to fill in the gaps.

## Running the API

```bash
brew install fastapi
fastapi dev main.py
```

Interactive docs available at `http://localhost:8000/docs`

---

## Endpoints

| Method | Endpoint | LeetCode Problem |
|--------|----------|-----------------|
| GET | `/` | Health check |
| POST | `/contains-duplicate-217` | 217. Contains Duplicate |

---

## NeetCode Problems

### Array & Hashing

| # | Problem | Difficulty | Solved in < 20 min |
|---|---------|:----------:|:------------------:|
| 217 | [Contains Duplicate](ArraysAndHashing/ContainsDuplicate_217.py) | Easy | ✅ |

---

## Project Structure

```
leetcode-solutions/
├── main.py                  # FastAPI app and routes
├── ArraysAndHashing/
│   └── ContainsDuplicate_217.py
└── README.md
```
