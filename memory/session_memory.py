session_memory = {
    "issues": [],
    "feedback": []
}

def remember_issue(issue):
    session_memory["issues"].append(issue)

def remember_feedback(line, description, accepted):
    session_memory["feedback"].append({
        "line": line,
        "description": description,
        "accepted": accepted
    })

def show_session_summary():
    print("\n🧠 Session Summary")
    print("-" * 40)
    print(f"Issues Found: {len(session_memory['issues'])}")
    for i, issue in enumerate(session_memory["issues"], 1):
        desc = issue.get("description") or issue.get("issue") or "No description provided"
        print(f"{i}. [Line {issue.get('line', '?')}] {desc}")

    print(f"\nUser Feedback:")
    for i, fb in enumerate(session_memory["feedback"], 1):
        status = "✅ Accepted" if fb["accepted"] else "❌ Rejected"
        print(f"{i}. Line {fb['line']}: {fb['description']} - {status}")