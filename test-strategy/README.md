# Sample Risk-Based Test Strategy

**Product:** Fictional mobile + web account service

## Goal

Find high-impact defects early while keeping feedback fast enough for frequent releases.

## Risk model

Assess each area using:
- **Customer impact:** How harmful would failure be?
- **Likelihood:** How likely is the failure given code changes, architecture, and defect history?
- **Detectability:** How easily would existing checks catch the failure?

Prioritize scenarios with high customer impact and high likelihood.

## Example test allocation

| Area | Risk | Test approach | Suggested layer |
|---|---|---|---|
| Input validation | Medium | Required, malformed, and boundary values | Unit + API |
| Authentication | High | Valid/invalid credentials, lockout, session expiry | Unit + API + focused E2E |
| Account data access | High | Authorization and access-control checks | API/integration |
| Network failures | Medium | Timeout, retry, offline recovery | Integration + mobile |
| Layout on devices | Medium | Supported screen sizes and OS versions | UI/device testing |
| Critical end-to-end journey | High | Sign-in through core user action | Small, stable E2E suite |

## CI recommendations

1. **On each change:** fast unit tests, linting, and relevant component tests.
2. **Before merge or in CI:** API and integration tests for affected areas.
3. **On a scheduled or release build:** broader device compatibility and end-to-end regression.
4. **Before release:** review open defects, test results, coverage gaps, and residual risks.

## Release readiness checklist

- [ ] Critical user journeys pass.
- [ ] High-risk areas have been tested.
- [ ] No unresolved release-blocking defects remain.
- [ ] Automated test failures are triaged, not blindly ignored.
- [ ] Known issues and residual risks are documented.
- [ ] Product and Engineering agree on release readiness.

## Important

This is a demonstration strategy. In a real project, test scope and gates should be adapted to architecture, product risk, change impact, service-level expectations, and release cadence.
