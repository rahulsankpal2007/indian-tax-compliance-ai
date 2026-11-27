import itertools

symbols = ["ITR", "TDS", "REF"]


def evaluate_kb(model):
    itr, tds, ref = model["ITR"], model["TDS"], model["REF"]
    rule1 = (not itr) or tds
    rule2 = (not tds) or ref
    fact1 = model["userItr"]
    fact2 = model["userTds"]
    return rule1 and rule2 and fact1 and fact2


def evaluate_query(model):
    return model["REF"]


def get_rejection_reason(user_itr, user_tds, counterexample):
    reasons = []
    if not user_itr:
        reasons.append(
            "• CRITICAL FAILURE: Income Tax Return (ITR) was not filed. By law, a refund cannot be initiated without an official tax filing."
        )
    if user_itr and not user_tds:
        reasons.append(
            "• RULE DISCONNECTED: ITR filed, but no excess Tax Deducted at Source (TDS) was detected. The legal chain to trigger a refund requires an overpayment."
        )
    if counterexample and not counterexample["REF"]:
        reasons.append(
            f"• LOGICAL LOOPHOLE FOUND: The truth table uncovered a vulnerable state where rules match but REF is False. "
            f"(Model state: ITR={counterexample['ITR']}, TDS={counterexample['TDS']}, REF={counterexample['REF']})"
        )
    return "\n".join(reasons)


def tt_entails(symbols, user_itr, user_tds):
    all_models = list(itertools.product([True, False], repeat=len(symbols)))
    kb_entails_query = True
    first_counterexample = None
    table_rows = []

    for combination in all_models:
        model = dict(zip(symbols, combination))
        model["userItr"] = user_itr
        model["userTds"] = user_tds

        kb_val = evaluate_kb(model)
        query_val = evaluate_query(model)
        table_rows.append(
            (model["ITR"], model["TDS"], model["REF"], kb_val, query_val)
        )

        if kb_val and not query_val:
            kb_entails_query = False
            if first_counterexample is None:
                first_counterexample = model

    return kb_entails_query, first_counterexample, table_rows


if __name__ == "__main__":
    print("=== Indian Tax Verification System Input Portal ===")
    itr_input = (
        input("Has the taxpayer filed the ITR? (yes/no): ").strip().lower()
    )
    tds_input = (
        input("Is there excess TDS deducted? (yes/no): ").strip().lower()
    )

    user_itr = itr_input in ["yes", "y", "true"]
    user_tds = tds_input in ["yes", "y", "true"]

    print("\nProcessing Entailment Verification Algorithms...\n")
    entailed, counterexample, rows = tt_entails(symbols, user_itr, user_tds)

    print("=== Indian Tax Compliance Verification Report ===")
    if entailed:
        print("Status: CLAIM APPROVED / ENTAILED ✅")
        print("Mathematical Proof: KB ⊨ REF (True)")
    else:
        print("Status: CLAIM REJECTED / NOT ENTAILED ❌")
        print("Mathematical Proof: KB ⊭ REF (False)")
        print("\n--- Diagnostic Rejection Reason ---")
        print(get_rejection_reason(user_itr, user_tds, counterexample))

    print("\nGenerated Compliance Truth Table Matrix:")
    print(f"{'ITR':<7} {'TDS':<7} {'REF':<7} {'KB':<7} {'Query(REF)'}")
    print("-" * 45)
    for itr, tds, ref, kb_val, q_val in rows:
        print(
            f"{str(itr):<7} {str(tds):<7} {str(ref):<7} {str(kb_val):<7} {str(q_val)}"
        )