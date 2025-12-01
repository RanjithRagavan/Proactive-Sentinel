from proactive_sentinel_agent.sub_agents.archivist_agent import scrub_pii

text = "my name is ranjith and my phone number is 124234"
scrubbed = scrub_pii(text)
print(f"Original: {text}")
print(f"Scrubbed: {scrubbed}")

if "ranjith" in scrubbed or "124234" in scrubbed:
    print("FAIL: PII not scrubbed")
else:
    print("SUCCESS: PII scrubbed")
