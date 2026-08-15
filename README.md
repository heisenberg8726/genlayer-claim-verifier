# GenLayer Claim Verifier

A reusable GenLayer Intelligent Contract for decentralized claim verification.

## Purpose

Claim Verifier allows users to submit a claim together with supporting evidence and verify the claim using GenLayer validator consensus.

## How It Works

1. A user submits a claim and evidence URL.
2. A leader evaluates the evidence.
3. Validators independently verify the result.
4. Validator results are compared using GenLayer consensus.
5. The accepted result is stored in contract state.

## Verification Results

- VERIFIED
- REJECTED
- UNCERTAIN

## State Design

Each claim stores:

- Claim text
- Evidence URL
- Verification status
- Confidence
- Explanation

## Consensus Logic

The contract uses independent validator evaluation rather than blindly accepting the leader's result.

## Testing

The project includes tests for:

- Verified claims
- Rejected claims
- Uncertain claims
- Validator agreement
- Validator disagreement
