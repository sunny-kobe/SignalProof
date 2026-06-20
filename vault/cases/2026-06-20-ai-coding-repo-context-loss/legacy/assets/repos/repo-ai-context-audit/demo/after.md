# After

> Synthetic example. This is the intended improvement after repo context audit.

The agent follows the repo-specific instructions:

```ts
const rows = users.map((user) => ({
  ...user,
  statusText: formatUserStatus(user.status),
}));
```

It uses `userApi.ts`, reuses `DataTable`, and preserves the `0 | 1` status contract.

## Improvements

- Reuses existing component.
- Preserves backend contract.
- Keeps API access in the existing API layer.
- Uses project formatter.
- Produces code that fits the repo rather than generic React code.
