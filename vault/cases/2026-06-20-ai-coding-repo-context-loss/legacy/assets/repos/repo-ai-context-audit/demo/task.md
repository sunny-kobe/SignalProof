# Synthetic Demo Task

> This is a synthetic task for demonstration only. It is not real user feedback.

## Repo Situation

A React admin project has:

- Existing `DataTable` component.
- Existing `formatUserStatus()` formatter.
- User API returns `status` as `0 | 1`, where `0` means disabled and `1` means enabled.
- Project convention requires page-level API calls through `userApi.ts`.

## Task

Add a user list page that displays user name, status, and created time.

## Expected Project-Specific Behavior

- Reuse `DataTable`.
- Reuse `formatUserStatus()`.
- Preserve `0 | 1` status semantics.
- Use `userApi.ts`.
- Do not invent boolean status.
