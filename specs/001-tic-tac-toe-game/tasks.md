# Tasks: Tic Tac Toe Game

**Input**: Design documents from `/specs/001-tic-tac-toe-game/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create project structure per implementation plan
- [ ] T002 [P] Create src/, src/ui/, and tests/ directories
- [ ] T003 [P] Add __init__.py files to src/, src/ui/, and tests/

---

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T004 [P] [US1] Define Mark, GameMode, GameStatus enums in src/models.py
- [ ] T005 [P] [US1] Define GameState dataclass in src/models.py
- [ ] T006 [P] [US1] Implement make_move, check_win, check_draw, get_computer_move, new_game in src/game_logic.py

---

## Phase 3: User Story 1 - Two Players Take Turns on a Shared Board (Priority: P1) 🎯 MVP

**Goal**: Two human players alternate turns on a 3×3 grid, with turn indication and move validation.
**Independent Test**: Two users can play a full game, alternating turns, with correct mark placement and turn switching.

- [ ] T007 [P] [US1] Implement test_models.py for GameState and enums in tests/test_models.py
- [ ] T008 [P] [US1] Implement test_game_logic.py for move validation, win/draw detection in tests/test_game_logic.py
- [ ] T009 [US1] Implement ModeScreen (mode selection) in src/ui/mode_screen.py
- [ ] T010 [US1] Implement GameScreen (3x3 grid, status label, New Game button) in src/ui/game_screen.py
- [ ] T011 [US1] Implement App class to manage screens in src/ui/app.py
- [ ] T012 [US1] Implement main entry point in src/main.py

---

## Phase 4: User Story 2 - Win Detection and Announcement (Priority: P1)

**Goal**: Detect three in a row, highlight winning squares, announce winner, and lock board.
**Independent Test**: Playing a winning sequence highlights the line, shows a win message, and disables further moves.

- [ ] T013 [P] [US2] Add win detection and winning line highlight to src/game_logic.py and src/ui/game_screen.py
- [ ] T014 [US2] Add win message display and board lock to src/ui/game_screen.py

---

## Phase 5: User Story 3 - Draw Detection (Priority: P1)

**Goal**: Detect full board with no winner, announce draw, and lock board.
**Independent Test**: Playing to a full board with no winner shows a draw message and disables further moves.

- [ ] T015 [P] [US3] Add draw detection to src/game_logic.py
- [ ] T016 [US3] Add draw message display and board lock to src/ui/game_screen.py

---

## Phase 6: User Story 4 - Start a New Game (Priority: P2)

**Goal**: Allow player to start a new game at any time, returning to mode selection and resetting state.
**Independent Test**: Clicking "New Game" returns to mode selection and resets the board and turn.

- [ ] T017 [US4] Implement "New Game" button to return to mode selection in src/ui/game_screen.py
- [ ] T018 [US4] Reset GameState and UI on new game in src/ui/app.py

---

## Phase 7: User Story 5 - Play Against the Computer (Priority: P2)

**Goal**: Player can play against a computer that makes random moves after the human.
**Independent Test**: In PvC mode, after the human moves, the computer automatically makes a valid move.

- [ ] T019 [P] [US5] Add GameMode.PVC support to src/models.py and src/ui/mode_screen.py
- [ ] T020 [US5] Implement computer move logic and auto-move after human in src/ui/game_screen.py

---


## Phase 8: Polish, Edge Cases & Accessibility

- [ ] T021 [P] Add docstrings and comments to all modules
- [ ] T022 [P] Manual GUI verification for all acceptance scenarios
- [ ] T023 [P] Add README usage instructions if needed

### UI Contract & Edge Case Tests
- [ ] T024 [P] [TEST] Test UI contract: mode selection screen has two buttons, game board is 3x3 grid, status label, New Game button, win highlight, board lock after win/draw
- [ ] T025 [P] [TEST] Test rapid clicks: verify only first valid click is accepted, no double-move or UI glitch
- [ ] T026 [P] [TEST] Test mode switch mid-game: switching mode resets game and returns to mode selection
- [ ] T027 [P] [TEST] Test computer move with only one empty square: computer always fills last square

### Accessibility
- [ ] T028 [P] [A11Y] Review keyboard navigation and color contrast in UI

----

## Dependencies

- Phase 1 and 2 must be complete before any user story phases
- User Story 1 is MVP and must be completed before later stories
- User Stories 2, 3 can be implemented in parallel after US1
- User Stories 4, 5 depend on US1-3

## Parallel Execution Examples

- T002, T003 can run in parallel
- T004, T005, T006 can run in parallel
- T007, T008 can run in parallel
- T013, T015, T021 can run in parallel

## Implementation Strategy

- MVP: Complete User Story 1 (T001–T012)
- Incrementally deliver each user story phase
- Each phase is independently testable and verifiable
