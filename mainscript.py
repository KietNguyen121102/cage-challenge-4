from CybORG import CybORG
from CybORG.Simulator.Scenarios import EnterpriseScenarioGenerator
from rich import print
import numpy as np
from CybORG.Agents.Wrappers import BlueFlatWrapper, BlueFixedActionWrapper


# Fixed agent tutorials

sg = EnterpriseScenarioGenerator()
cyborg = CybORG(scenario_generator=sg)


# env = BlueFixedActionWrapper(env=cyborg)
# obs, _ = env.reset()

# # print(obs.keys())
# # print(env.action_labels('blue_agent_0'))

# actions = {'blue_agent_0' : 45}
# obs, reward, terminated, truncated, inf = env.step(actions)
# print(reward['blue_agent_0'])


# messages = {'blue_agent_0' : np.array([1, 0, 0, 0, 0, 0, 0, 0])}
# obs, reward, terminated, truncated, info = env.step(actions, messages=messages)
# print(obs['blue_agent_1']['message'])


env = BlueFlatWrapper(env=cyborg)
obs, _ = env.reset()

print('Space:', env.observation_space('blue_agent_0'), '\n')
print('Observation:', obs['blue_agent_0'])