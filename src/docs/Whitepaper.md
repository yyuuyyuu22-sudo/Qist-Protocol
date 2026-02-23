# Whitepaper: Calculated Qist Protocol (CQP)
### Version 1.0 | February 2026

**Abstract:** The Calculated Qist Protocol (CQP) introduces a sovereign, post-quantum decentralized infrastructure designed to democratize AI compute resources. By separating "Execution" (High-performance hardware) from "Verification" (Low-performance hardware), CQP transforms idle consumer electronics into a global, unified intelligence engine.

---

## 1. System Architecture: The Sovereign Layer
CQP operates independently of legacy blockchains to eliminate external gas volatility and censorship risks.
* **P2P Protocol:** Utilizing a gossip-based discovery mechanism to link nodes globally.
* **Lattice-Based Cryptography:** CQP implements **CRYSTALS-Dilithium** for digital signatures, making the network "Quantum-Resistant" by design.

---

## 2. Functional Hierarchy: The Overseer Model
CQP implements a strictly enforced functional split to ensure fairness:

### A. Executors (The Workers)
* **Role:** Processing high-complexity AI inference and training tasks.
* **Requirement:** High-performance GPUs.
* **Incentive:** 80% of the task's minted reward.

### B. Overseers (The Judges)
* **Role:** Integrity verification and cross-validation of results.
* **Requirement:** Legacy PCs, Smartphones, or IoT devices.
* **Incentive:** 20% of the task's minted reward.

---

## 3. Consensus: Proof of Validated Work (PoVW)
The protocol replaces Hash-based competition with **Checkpointed Sampling Verification (CSV)**.
1. **Task Ingestion:** A request is fragmented into micro-tasks.
2. **State-Hashing:** The Executor generates state hashes at specific intervals.
3. **Probabilistic Audit:** Overseers randomly select a subset of these checkpoints and re-calculate them to verify the entire work.

---

## 4. Tokenomics: The Qist Unit (QU)
The **QU** is a non-inflationary utility token minted only upon successful work verification.
* **Zero Pre-mine:** No tokens exist until the first task is verified.
* **Fair Distribution:** Rewards are split 80/20 to balance energy costs and audit services.
