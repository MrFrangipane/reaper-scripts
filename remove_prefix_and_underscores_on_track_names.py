from reaper_python import * 


def get_track_names(proj_id: int = 0) -> list[str]:
  track_count =  RPR_CountTracks(proj_id)
  track_names = []

  for track_id in range(track_count):
    track = RPR_GetTrack(proj_id, track_id)
    track_names.append(RPR_GetTrackName(track, None, 50)[2])

  return track_names


def detect_prefix(items: list[str]) -> str:
  it = iter(items)
  try:
    prefix = next(it)
  except StopIteration:
    return ""

  for s in it:
    i = 0
    limit = min(len(prefix), len(s))
    while i < limit and prefix[i] == s[i]:
      i += 1
    prefix = prefix[:i]
    if not prefix:
      break
  return prefix


def set_track_name(proj_id: int, track_id: int, track_name: str):
    track = RPR_GetTrack(proj_id, track_id)
    RPR_GetSetMediaTrackInfo_String(track, 'P_NAME', track_name, 1)


def remove_prefix_and_underscores_on_track_names(proj_id: int = 0):
    track_names = get_track_names(proj_id)
    prefix = detect_prefix(list(track_names))
    for track_id, track_name in enumerate(track_names):
        new_track_name = track_name[len(prefix):]
        new_track_name = new_track_name.replace('_', ' ')
        set_track_name(proj_id, track_id, new_track_name)


if __name__ == "__main__":
    remove_prefix_and_underscores_on_track_names(proj_id=0)
