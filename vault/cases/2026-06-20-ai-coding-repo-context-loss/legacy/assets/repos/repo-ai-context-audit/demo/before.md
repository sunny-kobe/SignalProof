# Before

> Synthetic example. This is intentionally flawed to show the failure mode.

The agent creates a new table component instead of reusing `DataTable`, calls `fetch('/api/users')` directly, and converts `status` into boolean:

```ts
const enabled = Boolean(user.status);
```

## Problems

- Reimplements existing table behavior.
- Ignores `userApi.ts`.
- Changes `0 | 1` contract into boolean.
- Does not reuse `formatUserStatus()`.
- Looks reasonable in isolation but does not match the repo.
