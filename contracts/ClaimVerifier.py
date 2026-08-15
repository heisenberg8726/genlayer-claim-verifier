User
  │
  │ submit claim + evidence
  ▼
ClaimVerifier
  │
  ▼
Leader evaluates claim
  │
  ▼
Validators independently verify
  │
  ├── agree → VERIFIED
  │
  ├── reject → REJECTED
  │
  └── insufficient evidence → UNCERTAIN
  │
  ▼
Store result on-chain
