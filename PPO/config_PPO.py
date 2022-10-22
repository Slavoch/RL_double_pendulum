
config = {'max_episode_length': 200,
          'max_training_steps': 1e6,
          'max_number_of_epoch': 100,
          'update_timestep': 2000,
          'eps_clip': 0.2,
          'gamma': 0.99,
          'action_std': 0.6,
          'action_std_decay_rate': 0.05,
          'min_action_std': 0.1,
          'dt': 0.02,
          'lr_actor': 3e-4,
          'lr_critic': 1e-3,
          'save_model_freq': 1e5
          }