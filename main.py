def divorce_predictor():
    print("=" * 55)
    print("       💔 DIVORCE PREDICTOR TOOL 💔")
    print("   Based on Gottman's Relationship Research")
    print("=" * 55)
    print("Answer the following questions honestly.")
    print("Rate each using the scale below:")
    print("  1 = Never  | 2 = Rarely  | 3 = Sometimes")
    print("  4 = Often  | 5 = Always\n")

    questions = {
        "Communication Issues": [
            "Do you avoid talking about problems in your relationship?",
            "Do conversations often end without resolution?",
            "Do you feel unheard or ignored by your partner?",
        ],
        "Criticism & Contempt": [
            "Do you or your partner criticize each other's personality?",
            "Is there eye-rolling, sarcasm, or mockery in arguments?",
            "Do you feel disrespected by your partner?",
        ],
        "Defensiveness & Stonewalling": [
            "Do you or your partner get defensive during disagreements?",
            "Does one of you shut down or give the silent treatment?",
            "Do you refuse to accept responsibility in conflicts?",
        ],
        "Emotional Connection": [
            "Do you feel emotionally distant from your partner?",
            "Has intimacy (physical or emotional) decreased significantly?",
            "Do you feel lonely even when together?",
        ],
        "Trust & Respect": [
            "Do you doubt your partner's honesty or loyalty?",
            "Do you feel disrespected by your partner regularly?",
            "Have there been incidents of betrayal or infidelity?",
        ],
        "Future & Goals": [
            "Do you have very different life goals or values?",
            "Do you rarely plan or look forward to a future together?",
            "Do you feel happier when your partner is not around?",
        ],
    }

    scores = {}
    total_score = 0
    max_score = 0

    for category, qs in questions.items():
        print(f"\n📌 {category}")
        print("-" * 40)
        category_score = 0
        for q in qs:
            while True:
                try:
                    ans = int(input(f"  {q}\n  → (1=Never, 2=Rarely, 3=Sometimes, 4=Often, 5=Always): "))
                    if 1 <= ans <= 5:
                        category_score += ans
                        break
                    else:
                        print("  ⚠ Please enter a number between 1 and 5.")
                except ValueError:
                    print("  ⚠ Invalid input! Enter a number between 1 and 5.")
        scores[category] = category_score
        total_score += category_score
        max_score += len(qs) * 5

    # ─── Results ───────────────────────────────────────────
    percentage = (total_score / max_score) * 100

    print("\n" + "=" * 55)
    print("           📊 YOUR RESULTS")
    print("=" * 55)

    print(f"\n{'Category':<30} {'Score':>6}  {'Risk'}")
    print("-" * 55)
    for cat, score in scores.items():
        max_cat = 15  # 3 questions × 5
        pct = (score / max_cat) * 100
        if pct >= 70:
            risk = "🔴 High"
        elif pct >= 40:
            risk = "🟡 Medium"
        else:
            risk = "🟢 Low"
        print(f"{cat:<30} {score:>4}/15  {risk}")

    print("-" * 55)
    print(f"{'TOTAL SCORE':<30} {total_score:>4}/{max_score}")

    # ─── Overall Prediction ────────────────────────────────
    print("\n" + "=" * 55)
    print("        🔮 DIVORCE RISK PREDICTION")
    print("=" * 55)

    if percentage >= 75:
        print(f"\n  Risk Level   : 🔴 VERY HIGH ({percentage:.1f}%)")
        print("  Prediction   : Relationship is in serious danger.")
        print("  Advice       : Seek couples therapy immediately.")
        print("                 Open, honest communication is critical.")
    elif percentage >= 55:
        print(f"\n  Risk Level   : 🟠 HIGH ({percentage:.1f}%)")
        print("  Prediction   : Significant issues need attention.")
        print("  Advice       : Consider professional counseling.")
        print("                 Work on rebuilding trust and respect.")
    elif percentage >= 35:
        print(f"\n  Risk Level   : 🟡 MODERATE ({percentage:.1f}%)")
        print("  Prediction   : Some problems but manageable.")
        print("  Advice       : Have honest conversations with your partner.")
        print("                 Focus on improving communication.")
    else:
        print(f"\n  Risk Level   : 🟢 LOW ({percentage:.1f}%)")
        print("  Prediction   : Relationship appears stable.")
        print("  Advice       : Keep nurturing your bond.")
        print("                 Regular check-ins keep relationships healthy.")

    # ─── Weakest Area ──────────────────────────────────────
    weakest = max(scores, key=scores.get)
    print(f"\n  ⚠  Area Needing Most Attention: {weakest}")

    print("\n" + "=" * 55)
    print("  ⚠  DISCLAIMER: This tool is for educational")
    print("     purposes only and is NOT a substitute for")
    print("     professional relationship counseling.")
    print("=" * 55)

    # ─── Retry ─────────────────────────────────────────────
    again = input("\n🔄 Take the test again? (yes/no): ").strip().lower()
    if again == 'yes':
        divorce_predictor()
    else:
        print("\n💙 Take care of yourself and your relationships. Goodbye!\n")


divorce_predictor()
