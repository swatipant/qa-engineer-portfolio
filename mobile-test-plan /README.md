# Sample Mobile Application Test Plan

**Scenario:** A fictional mobile application with sign-in and a user profile.

## Scope

Validate core sign-in behavior, session handling, network interruptions, and compatibility across supported devices.

## Sample test scenarios

| ID | Scenario | Steps / Test Data | Expected Result | Priority |
|---|---|---|---|---|
| MOB-001 | Valid sign-in | Enter valid test credentials | User signs in and reaches the home screen | P0 |
| MOB-002 | Invalid password | Enter a valid username and incorrect password | Clear error appears; user remains signed out | P0 |
| MOB-003 | Empty required fields | Submit with username and password empty | Required-field validation appears | P1 |
| MOB-004 | Network interruption | Disable network during sign-in | App handles the failure gracefully and offers retry | P1 |
| MOB-005 | Session after app restart | Sign in, close and reopen app | Behavior matches the documented session policy | P1 |
| MOB-006 | Device compatibility | Repeat core flow on supported OS/device combinations | Core behavior remains consistent | P1 |
| MOB-007 | Repeated submit | Tap sign-in multiple times quickly | No duplicate request or inconsistent UI state | P1 |

## Entry criteria

- Test build and environment are available.
- Requirements and supported device/OS matrix are documented.
- Test accounts and test data are ready.

## Exit criteria

- All P0 scenarios pass.
- No unresolved release-blocking defects remain.
- High-severity failures have documented disposition and approval.
- Results, known issues, and residual risks are shared with stakeholders.

## Notes

This is a sample plan for a fictional app, not a record of testing a real product.
