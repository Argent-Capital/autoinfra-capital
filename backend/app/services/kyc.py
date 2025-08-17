def verify_kyc(document_hash: str) -> str:
    # Mock: accept anything with even last hex as 'verified'
    try:
        last = int(document_hash[-1], 16)
        return "verified" if last % 2 == 0 else "review"
    except Exception:
        return "rejected"
