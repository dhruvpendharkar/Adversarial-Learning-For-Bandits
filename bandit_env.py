import numpy as np

class BanditEnv():
  def __init__(self, k):
    self.arms = k
    self.rewards = np.random.uniform(0, 1, k)
    self.variances = np.random.uniform(0.1, 0.5, k)

  def get_reward(self, arm):
    return np.random.normal(self.rewards[arm], self.variances[arm])