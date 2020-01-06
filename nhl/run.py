import nhl.raw

print(nhl.raw.stats.awards.get())

print(nhl.raw.stats.conferences.get())

divisions = nhl.raw.stats.divisions.get()
print(divisions)
print(divisions.divisions[0].conference.follow_link())
