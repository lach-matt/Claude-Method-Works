---
type: "query"
date: "2026-09-02T14:35:42.166029+00:00"
question: "Which files in this corpus restate the same content under different names?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["The Languages", "The Six Languages", "Description Length", "Slack", "Mathematical Compendium", "The Method 1.6"]
---

# Q: Which files in this corpus restate the same content under different names?

## Answer

math.pdf (the Mathematical Compendium) and "The Method 1.6.md" (the main book) describe the SAME structures in different vocabulary. Every one of the graph's top surprising connections is a semantically_similar_to edge crossing between these two files:
- "The Languages" (math.pdf) <-> "The Six Languages" (book)
- "Description Length" (math.pdf) <-> "Slack" (book)
- "Slack" <-> "Slack"
- "Staircase Connected Row-Convex" <-> "The Staircase Constraint"
- "The Register as an Index" <-> "The Register"

Navigational consequence: the compendium is the formal/object-level statement (objects named S.*, Q.*, L.*, A.*, K.* with grade, source, depends-on and depth fields) and the book is the prose statement of the same content. When a query hits one, check the other for the counterpart under a different name. The compendium's object headers carry the machine-readable dependency graph (depends on X, N objects depend on it, depth D) and are the best source for "what rests on what".

## Outcome

- Signal: useful

## Source Nodes

- The Languages
- The Six Languages
- Description Length
- Slack
- Mathematical Compendium
- The Method 1.6