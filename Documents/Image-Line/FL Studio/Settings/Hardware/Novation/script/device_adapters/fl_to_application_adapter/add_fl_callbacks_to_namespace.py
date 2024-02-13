def add_fl_callbacks_to_namespace(namespace, adapter):
    namespace["OnInit"] = adapter.on_init
    namespace["OnDeInit"] = adapter.on_deinit
    namespace["OnMidiIn"] = adapter.on_midi
    namespace["OnRefresh"] = adapter.on_refresh
    namespace["OnIdle"] = adapter.on_idle
    namespace["OnDirtyChannel"] = adapter.on_dirty_channel
    namespace["OnDirtyMixerTrack"] = adapter.on_dirty_mixer_track
    namespace["OnProjectLoad"] = adapter.on_project_load
    namespace["OnFirstConnect"] = adapter.on_first_connect