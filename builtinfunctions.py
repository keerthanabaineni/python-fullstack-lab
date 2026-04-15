
raw_payload = "     GhostAdmin | 7 | failed_login     "
clean_payload = raw_payload.strip()
parts=clean_payload.split(" | ")
username=parts[0].strip()
sector_id=parts[1].strip()
status=parts[2].strip()
if username.isalnum():
    print("{} {} failed_login in sector {}".format(username, status, sector_id))
else:
    print("LOCKDOWN INITIALIZED")



