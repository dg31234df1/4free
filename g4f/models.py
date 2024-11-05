from __future__  import annotations

from dataclasses import dataclass

from .Provider import IterListProvider, ProviderType
from .Provider import (
    Ai4Chat,
    AIChatFree,
    AiMathGPT,
    Airforce,
    AIUncensored,
    Allyfy,
    Bing,
    Blackbox,
    ChatGpt,
    Chatgpt4Online,
    ChatGptEs,
    ChatifyAI,
    Cloudflare,
    DarkAI,
    DDG,
    DeepInfra,
    DeepInfraChat,
    Editee,
    Free2GPT,
    FreeChatgpt,
    FreeGpt,
    FreeNetfly,
    Gemini,
    GeminiPro,
    GizAI,
    GigaChat,
    GPROChat,
    HuggingChat,
    HuggingFace,
    Koala,
    Liaobots,
    MagickPen,
    MetaAI,
    NexraBing,
    NexraBlackbox,
    NexraChatGPT,
    NexraDallE,
    NexraDallE2,
    NexraEmi,
    NexraFluxPro,
    NexraGeminiPro,
    NexraMidjourney,
    NexraQwen,
    NexraSD15,
    NexraSDLora,
    NexraSDTurbo,
    OpenaiChat,
    PerplexityLabs,
    Pi,
    Pizzagpt,
    Reka,
    Replicate,
    ReplicateHome,
    RubiksAI,
    TeachAnything,
    Upstage,
)


@dataclass(unsafe_hash=True)
class Model:
    """
    Represents a machine learning model configuration.

    Attributes:
        name (str): Name of the model.
        base_provider (str): Default provider for the model.
        best_provider (ProviderType): The preferred provider for the model, typically with retry logic.
    """
    name: str
    base_provider: str
    best_provider: ProviderType = None

    @staticmethod
    def __all__() -> list[str]:
        """Returns a list of all model names."""
        return _all_models


### Default ###
default = Model(
    name          = "",
    base_provider = "",
    best_provider = IterListProvider([
        DDG,
        FreeChatgpt,
        HuggingChat,
        Pizzagpt,
        ReplicateHome,
        Upstage,
        Blackbox,
        Free2GPT,
        MagickPen,
        DeepInfraChat,
        Airforce, 
        ChatGptEs,
        ChatifyAI,
        Cloudflare,
        Editee,
        AiMathGPT,
        AIUncensored,
    ])
)



############
### Text ###
############

### OpenAI ###
# gpt-3
gpt_3 = Model(
    name          = 'gpt-3',
    base_provider = 'OpenAI',
    best_provider = NexraChatGPT
)

# gpt-3.5
gpt_35_turbo = Model(
    name          = 'gpt-3.5-turbo',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DarkAI, NexraChatGPT, Airforce, Liaobots, Allyfy])
)

# gpt-4
gpt_4o = Model(
    name          = 'gpt-4o',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, ChatGptEs, DarkAI, Editee, NexraChatGPT, Airforce, ChatGpt, Liaobots, OpenaiChat])
)

gpt_4o_mini = Model(
    name          = 'gpt-4o-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, ChatGptEs, FreeNetfly, Pizzagpt, MagickPen, RubiksAI, Liaobots, ChatGpt, Airforce, Koala, OpenaiChat])
)

gpt_4_turbo = Model(
    name          = 'gpt-4-turbo',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Liaobots, Airforce, ChatGpt, Bing])
)

gpt_4 = Model(
    name          = 'gpt-4',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Chatgpt4Online, Ai4Chat, NexraBing, NexraChatGPT, ChatGpt, Airforce, Bing, OpenaiChat, gpt_4_turbo.best_provider, gpt_4o.best_provider, gpt_4o_mini.best_provider])
)

# o1
o1 = Model(
    name          = 'o1',
    base_provider = 'OpenAI',
    best_provider = None
)

o1_mini = Model(
    name          = 'o1-mini',
    base_provider = 'OpenAI',
    best_provider = None
)


### GigaChat ###
gigachat = Model(
    name          = 'GigaChat:latest',
    base_provider = 'gigachat',
    best_provider = GigaChat
)


### Meta ###
meta = Model(
    name          = "meta-ai",
    base_provider = "Meta",
    best_provider = MetaAI
)

# llama 2
llama_2_7b = Model(
    name          = "llama-2-7b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Cloudflare, Airforce])
)

llama_2_13b = Model(
    name          = "llama-2-13b",
    base_provider = "Meta Llama",
    best_provider = Airforce
)

# llama 3
llama_3_8b = Model(
    name          = "llama-3-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Cloudflare, Airforce, DeepInfra, Replicate])
)

llama_3_70b = Model(
    name          = "llama-3-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([ReplicateHome, Airforce, DeepInfra, Replicate])
)

# llama 3.1
llama_3_1_8b = Model(
    name          = "llama-3.1-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Blackbox, DeepInfraChat, Cloudflare, Airforce, PerplexityLabs])
)

llama_3_1_70b = Model(
    name          = "llama-3.1-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DDG, HuggingChat, Blackbox, FreeGpt, TeachAnything, Free2GPT, DeepInfraChat, DarkAI, AiMathGPT, RubiksAI, Airforce, HuggingFace, PerplexityLabs])
)

llama_3_1_405b = Model(
    name          = "llama-3.1-405b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat, Blackbox, DarkAI, Airforce])
)

# llama 3.2
llama_3_2_1b = Model(
    name          = "llama-3.2-1b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Cloudflare, Airforce])
)

llama_3_2_3b = Model(
    name          = "llama-3.2-3b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Cloudflare, Airforce])
)

llama_3_2_11b = Model(
    name          = "llama-3.2-11b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Cloudflare, HuggingChat, Airforce, HuggingFace])
)

llama_3_2_90b = Model(
    name          = "llama-3.2-90b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Airforce])
)


# llamaguard
llamaguard_7b = Model(
    name          = "llamaguard-7b",
    base_provider = "Meta Llama",
    best_provider = Airforce
)

llamaguard_2_8b = Model(
    name          = "llamaguard-2-8b",
    base_provider = "Meta Llama",
    best_provider = Airforce
)

llamaguard_3_8b = Model(
    name          = "llamaguard-3-8b",
    base_provider = "Meta Llama",
    best_provider = Airforce
)

llamaguard_3_11b = Model(
    name          = "llamaguard-3-11b",
    base_provider = "Meta Llama",
    best_provider = Airforce
)


### Mistral ###
mistral_7b = Model(
    name          = "mistral-7b",
    base_provider = "Mistral",
    best_provider = IterListProvider([DeepInfraChat, Cloudflare, Airforce, DeepInfra])
)

mixtral_8x7b = Model(
    name          = "mixtral-8x7b",
    base_provider = "Mistral",
    best_provider = IterListProvider([DDG, ReplicateHome, DeepInfraChat, Airforce, DeepInfra])
)

mixtral_8x22b = Model(
    name          = "mixtral-8x22b",
    base_provider = "Mistral",
    best_provider = IterListProvider([DeepInfraChat, Airforce])
)

mistral_nemo = Model(
    name          = "mistral-nemo",
    base_provider = "Mistral",
    best_provider = IterListProvider([HuggingChat, HuggingFace])
)

mistral_large = Model(
    name          = "mistral-large",
    base_provider = "Mistral",
    best_provider = IterListProvider([Editee])
)


### NousResearch ###
hermes_2 = Model(
    name          = "hermes-2",
    base_provider = "NousResearch",
    best_provider = Airforce
)

hermes_2_dpo = Model(
    name          = "hermes-2-dpo",
    base_provider = "NousResearch",
    best_provider = Airforce
)

hermes_3 = Model(
    name          = "hermes-3",
    base_provider = "NousResearch",
    best_provider = IterListProvider([HuggingChat, HuggingFace])
)


### Microsoft ###
phi_2 = Model(
    name          = "phi-2",
    base_provider = "Microsoft",
    best_provider = IterListProvider([Cloudflare, Airforce])
)

phi_3_medium_4k = Model(
    name          = "phi-3-medium-4k",
    base_provider = "Microsoft",
    best_provider = DeepInfraChat
)

phi_3_5_mini = Model(
    name          = "phi-3.5-mini",
    base_provider = "Microsoft",
    best_provider = IterListProvider([HuggingChat, HuggingFace])
)

### Google DeepMind ###
# gemini
gemini_pro = Model(
    name          = 'gemini-pro',
    base_provider = 'Google DeepMind',
    best_provider = IterListProvider([GeminiPro, Blackbox, AIChatFree, GPROChat, NexraGeminiPro, Editee, Airforce, Liaobots])
)

gemini_flash = Model(
    name          = 'gemini-flash',
    base_provider = 'Google DeepMind',
    best_provider = IterListProvider([Blackbox, GizAI, Airforce, Liaobots])
)

gemini = Model(
    name          = 'gemini',
    base_provider = 'Google DeepMind',
    best_provider = Gemini
)

# gemma
gemma_2b = Model(
    name          = 'gemma-2b',
    base_provider = 'Google',
    best_provider = IterListProvider([ReplicateHome, Airforce])
)

gemma_2b_27b = Model(
    name          = 'gemma-2b-27b',
    base_provider = 'Google',
    best_provider = IterListProvider([DeepInfraChat, Airforce])
)

gemma_7b = Model(
    name          = 'gemma-7b',
    base_provider = 'Google',
    best_provider = Cloudflare
)

# gemma 2
gemma_2_9b = Model(
    name          = 'gemma-2-9b',
    base_provider = 'Google',
    best_provider = Airforce
)


### Anthropic ###
claude_2_1 = Model(
    name          = 'claude-2.1',
    base_provider = 'Anthropic',
    best_provider = Liaobots
)

# claude 3
claude_3_opus = Model(
    name          = 'claude-3-opus',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Liaobots])
)

claude_3_sonnet = Model(
    name          = 'claude-3-sonnet',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Liaobots])
)

claude_3_haiku = Model(
    name          = 'claude-3-haiku',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([DDG, Liaobots])
)

# claude 3.5
claude_3_5_sonnet = Model(
    name          = 'claude-3.5-sonnet',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Blackbox, Editee, Liaobots])
)


### Reka AI ###
reka_core = Model(
    name = 'reka-core',
    base_provider = 'Reka AI',
    best_provider = Reka
)


### Blackbox AI ###
blackboxai = Model(
    name = 'blackboxai',
    base_provider = 'Blackbox AI',
    best_provider = IterListProvider([Blackbox, NexraBlackbox])
)

blackboxai_pro = Model(
    name = 'blackboxai-pro',
    base_provider = 'Blackbox AI',
    best_provider = Blackbox
)


### Databricks ###
dbrx_instruct = Model(
    name = 'dbrx-instruct',
    base_provider = 'Databricks',
    best_provider = IterListProvider([Airforce, DeepInfra])
)


### CohereForAI ###
command_r_plus = Model(
    name = 'command-r-plus',
    base_provider = 'CohereForAI',
    best_provider = HuggingChat
)


### iFlytek ###
sparkdesk_v1_1 = Model(
    name = 'sparkdesk-v1.1',
    base_provider = 'iFlytek',
    best_provider = FreeChatgpt
)


### Qwen ###
# qwen 1
qwen_1_5_0_5b = Model(
    name = 'qwen-1.5-0.5b',
    base_provider = 'Qwen',
    best_provider = Cloudflare
)

qwen_1_5_7b = Model(
    name = 'qwen-1.5-7b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Cloudflare])
)

qwen_1_5_14b = Model(
    name = 'qwen-1.5-14b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([FreeChatgpt, Cloudflare])
)

# qwen 2
qwen_2_72b = Model(
    name = 'qwen-2-72b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingChat, Airforce, HuggingFace])
)

qwen_2_5_7b = Model(
    name = 'qwen-2-5-7b',
    base_provider = 'Qwen',
    best_provider = Airforce
)

qwen_2_5_72b = Model(
    name = 'qwen-2-5-72b',
    base_provider = 'Qwen',
    best_provider = Airforce
)

qwen = Model(
    name = 'qwen',
    base_provider = 'Qwen',
    best_provider = NexraQwen
)


### Zhipu AI ###
glm_3_6b = Model(
    name = 'glm-3-6b',
    base_provider = 'Zhipu AI',
    best_provider = FreeChatgpt
)

glm_4_9b = Model(
    name = 'glm-4-9B',
    base_provider = 'Zhipu AI',
    best_provider = FreeChatgpt
)


### 01-ai ###
yi_1_5_9b = Model(
    name = 'yi-1.5-9b',
    base_provider = '01-ai',
    best_provider = FreeChatgpt
)

### Upstage ###
solar_10_7b = Model(
    name = 'solar-10-7b',
    base_provider = 'Upstage',
    best_provider = Airforce
)

solar_mini = Model(
    name = 'solar-mini',
    base_provider = 'Upstage',
    best_provider = Upstage
)

solar_pro = Model(
    name = 'solar-pro',
    base_provider = 'Upstage',
    best_provider = Upstage
)


### Inflection ###
pi = Model(
    name = 'pi',
    base_provider = 'Inflection',
    best_provider = Pi
)

### DeepSeek ###
deepseek_coder = Model(
    name = 'deepseek-coder',
    base_provider = 'DeepSeek',
    best_provider = Airforce
)

### WizardLM ###
wizardlm_2_7b = Model(
    name = 'wizardlm-2-7b',
    base_provider = 'WizardLM',
    best_provider = DeepInfraChat
)

wizardlm_2_8x22b = Model(
    name = 'wizardlm-2-8x22b',
    base_provider = 'WizardLM',
    best_provider = IterListProvider([DeepInfraChat, Airforce])
)

### Yorickvp ###
llava_13b = Model(
    name = 'llava-13b',
    base_provider = 'Yorickvp',
    best_provider = ReplicateHome
)


### OpenBMB ###
minicpm_llama_3_v2_5 = Model(
    name = 'minicpm-llama-3-v2.5',
    base_provider = 'OpenBMB',
    best_provider = DeepInfraChat
)


### Lzlv ###
lzlv_70b = Model(
    name = 'lzlv-70b',
    base_provider = 'Lzlv',
    best_provider = DeepInfraChat
)


### OpenChat ###
openchat_3_5 = Model(
    name = 'openchat-3.5',
    base_provider = 'OpenChat',
    best_provider = IterListProvider([Cloudflare])
)

openchat_3_6_8b = Model(
    name = 'openchat-3.6-8b',
    base_provider = 'OpenChat',
    best_provider = DeepInfraChat
)


### Phind ###
phind_codellama_34b_v2 = Model(
    name = 'phind-codellama-34b-v2',
    base_provider = 'Phind',
    best_provider = DeepInfraChat
)


### Cognitive Computations ###
dolphin_2_9_1_llama_3_70b = Model(
    name = 'dolphin-2.9.1-llama-3-70b',
    base_provider = 'Cognitive Computations',
    best_provider = DeepInfraChat
)


### x.ai ###
grok_2 = Model(
    name = 'grok-2',
    base_provider = 'x.ai',
    best_provider = Liaobots
)

grok_2_mini = Model(
    name = 'grok-2-mini',
    base_provider = 'x.ai',
    best_provider = Liaobots
)


### Perplexity AI ### 
sonar_online = Model(
    name = 'sonar-online',
    base_provider = 'Perplexity AI',
    best_provider = IterListProvider([PerplexityLabs])
)

sonar_chat = Model(
    name = 'sonar-chat',
    base_provider = 'Perplexity AI',
    best_provider = PerplexityLabs
)

### TheBloke ### 
german_7b = Model(
    name = 'german-7b',
    base_provider = 'TheBloke',
    best_provider = Cloudflare
)


### Fblgit ### 
cybertron_7b = Model(
    name = 'cybertron-7b',
    base_provider = 'Fblgit',
    best_provider = Cloudflare
)


### Nvidia ### 
nemotron_70b = Model(
    name = 'nemotron-70b',
    base_provider = 'Nvidia',
    best_provider = IterListProvider([HuggingChat, HuggingFace])
)


### Teknium ### 
openhermes_2_5 = Model(
    name = 'openhermes-2.5',
    base_provider = 'Teknium',
    best_provider = Airforce
)


### Pawan ### 
cosmosrp = Model(
    name = 'cosmosrp',
    base_provider = 'Pawan',
    best_provider = Airforce
)


### Liquid ### 
lfm_40b = Model(
    name = 'lfm-40b',
    base_provider = 'Liquid',
    best_provider = Airforce
)


### DiscoResearch ### 
german_7b = Model(
    name = 'german-7b',
    base_provider = 'DiscoResearch',
    best_provider = Airforce
)


### HuggingFaceH4 ### 
zephyr_7b = Model(
    name = 'zephyr-7b',
    base_provider = 'HuggingFaceH4',
    best_provider = Airforce
)



#############
### Image ###
#############

### Stability AI ###
sdxl_turbo = Model(
    name = 'sdxl-turbo',
    base_provider = 'Stability AI',
    best_provider = NexraSDTurbo
    
)

sdxl_lora = Model(
    name = 'sdxl-lora',
    base_provider = 'Stability AI',
    best_provider = NexraSDLora
    
)

sdxl = Model(
    name = 'sdxl',
    base_provider = 'Stability AI',
    best_provider = IterListProvider([ReplicateHome, Airforce])
    
)

sd_1_5 = Model(
    name = 'sd-1.5',
    base_provider = 'Stability AI',
    best_provider = IterListProvider([NexraSD15])
    
)

sd_3 = Model(
    name = 'sd-3',
    base_provider = 'Stability AI',
    best_provider = ReplicateHome
    
)

### Playground ###
playground_v2_5 = Model(
    name = 'playground-v2.5',
    base_provider = 'Playground AI',
    best_provider = ReplicateHome
    
)


### Flux AI ###
flux = Model(
    name = 'flux',
    base_provider = 'Flux AI',
    best_provider = IterListProvider([Blackbox, AIUncensored, Airforce])
    
)

flux_pro = Model(
    name = 'flux-pro',
    base_provider = 'Flux AI',
    best_provider = IterListProvider([NexraFluxPro])
    
)

flux_realism = Model(
    name = 'flux-realism',
    base_provider = 'Flux AI',
    best_provider = IterListProvider([Airforce])
    
)

flux_anime = Model(
    name = 'flux-anime',
    base_provider = 'Flux AI',
    best_provider = Airforce
    
)

flux_3d = Model(
    name = 'flux-3d',
    base_provider = 'Flux AI',
    best_provider = Airforce
    
)

flux_disney = Model(
    name = 'flux-disney',
    base_provider = 'Flux AI',
    best_provider = Airforce
    
)

flux_pixel = Model(
    name = 'flux-pixel',
    base_provider = 'Flux AI',
    best_provider = Airforce
    
)

flux_4o = Model(
    name = 'flux-4o',
    base_provider = 'Flux AI',
    best_provider = Airforce
    
)

flux_schnell = Model(
    name = 'flux-schnell',
    base_provider = 'Flux AI',
    best_provider = IterListProvider([ReplicateHome])
    
)


### OpenAI ###
dalle_2 = Model(
    name = 'dalle-2',
    base_provider = 'OpenAI',
    best_provider = NexraDallE2
    
)

dalle = Model(
    name = 'dalle',
    base_provider = 'OpenAI',
    best_provider = NexraDallE
    
)

### Midjourney ###
midjourney = Model(
    name = 'midjourney',
    base_provider = 'Midjourney',
    best_provider = NexraMidjourney
    
)

### Other ###
emi = Model(
    name = 'emi',
    base_provider = '',
    best_provider = NexraEmi
    
)

any_dark = Model(
    name = 'any-dark',
    base_provider = '',
    best_provider = Airforce
    
)

class ModelUtils:
    """
    Utility class for mapping string identifiers to Model instances.

    Attributes:
        convert (dict[str, Model]): Dictionary mapping model string identifiers to Model instances.
    """
    convert: dict[str, Model] = {
    
############
### Text ###
############
        
### OpenAI ###
# gpt-3
'gpt-3': gpt_3,

# gpt-3.5
'gpt-3.5-turbo': gpt_35_turbo,

# gpt-4
'gpt-4o': gpt_4o,
'gpt-4o-mini': gpt_4o_mini,
'gpt-4': gpt_4,
'gpt-4-turbo': gpt_4_turbo,

# o1
'o1': o1,
'o1-mini': o1_mini,
       
        
### Meta ###
"meta-ai": meta,

# llama-2
'llama-2-7b': llama_2_7b,
'llama-2-13b': llama_2_13b,

# llama-3
'llama-3-8b': llama_3_8b,
'llama-3-70b': llama_3_70b,
        
# llama-3.1
'llama-3.1-8b': llama_3_1_8b,
'llama-3.1-70b': llama_3_1_70b,
'llama-3.1-405b': llama_3_1_405b,

# llama-3.2
'llama-3.2-1b': llama_3_2_1b,
'llama-3.2-3b': llama_3_2_3b,
'llama-3.2-11b': llama_3_2_11b,
'llama-3.2-90b': llama_3_2_90b,

# llamaguard
'llamaguard-7b': llamaguard_7b,
'llamaguard-2-8b': llamaguard_2_8b,
'llamaguard-3-8b': llamaguard_3_8b,
'llamaguard-3-11b': llamaguard_3_11b,
      
        
### Mistral ###
'mistral-7b': mistral_7b,
'mixtral-8x7b': mixtral_8x7b,
'mixtral-8x22b': mixtral_8x22b,
'mistral-nemo': mistral_nemo,
'mistral-large': mistral_large,
     
     
### NousResearch ###
'hermes-2': hermes_2,
'hermes-2-dpo': hermes_2_dpo,
'hermes-3': hermes_3,

                
### Microsoft ###
'phi-2': phi_2,
'phi_3_medium-4k': phi_3_medium_4k,
'phi-3.5-mini': phi_3_5_mini,


### Google ###
# gemini
'gemini': gemini,
'gemini-pro': gemini_pro,
'gemini-flash': gemini_flash,
        
# gemma
'gemma-2b': gemma_2b,
'gemma-2b-27b': gemma_2b_27b,
'gemma-7b': gemma_7b,

# gemma-2
'gemma-2-9b': gemma_2_9b,


### Anthropic ###
'claude-2.1': claude_2_1,

# claude 3
'claude-3-opus': claude_3_opus,
'claude-3-sonnet': claude_3_sonnet,
'claude-3-haiku': claude_3_haiku,

# claude 3.5
'claude-3.5-sonnet': claude_3_5_sonnet,
        
        
### Reka AI ###
'reka-core': reka_core,
      
        
### Blackbox AI ###
'blackboxai': blackboxai,
'blackboxai-pro': blackboxai_pro,
        
        
### CohereForAI ###
'command-r+': command_r_plus,
        
        
### Databricks ###
'dbrx-instruct': dbrx_instruct,


### GigaChat ###
'gigachat': gigachat,
        
        
### iFlytek ###
'sparkdesk-v1.1': sparkdesk_v1_1,
        
        
### Qwen ###
'qwen': qwen,
'qwen-1.5-0.5b': qwen_1_5_0_5b,
'qwen-1.5-7b': qwen_1_5_7b,
'qwen-1.5-14b': qwen_1_5_14b,
'qwen-2-72b': qwen_2_72b,
'qwen-2-5-7b': qwen_2_5_7b,
'qwen-2-5-72b': qwen_2_5_72b,
        
        
### Zhipu AI ###
'glm-3-6b': glm_3_6b,
'glm-4-9b': glm_4_9b,
        
        
### 01-ai ###
'yi-1.5-9b': yi_1_5_9b,
        
        
### Upstage ###
'solar-10-7b': solar_10_7b,
'solar-mini': solar_mini,
'solar-pro': solar_pro,


### Inflection ###
'pi': pi,


### DeepSeek ###
'deepseek-coder': deepseek_coder,
     
        
### Yorickvp ###
'llava-13b': llava_13b,


### WizardLM ###
'wizardlm-2-7b': wizardlm_2_7b,
'wizardlm-2-8x22b': wizardlm_2_8x22b,
      
        
### OpenBMB ###
'minicpm-llama-3-v2.5': minicpm_llama_3_v2_5,
        
        
### Lzlv ###
'lzlv-70b': lzlv_70b,
     
        
### OpenChat ###
'openchat-3.5': openchat_3_5,
'openchat-3.6-8b': openchat_3_6_8b,


### Phind ###
'phind-codellama-34b-v2': phind_codellama_34b_v2,
        
        
### Cognitive Computations ###
'dolphin-2.9.1-llama-3-70b': dolphin_2_9_1_llama_3_70b,
    
        
### x.ai ###
'grok-2': grok_2,
'grok-2-mini': grok_2_mini,
        
        
### Perplexity AI ###
'sonar-online': sonar_online,
'sonar-chat': sonar_chat,
     
        
### TheBloke ###   
'german-7b': german_7b,


### Fblgit ###   
'cybertron-7b': cybertron_7b,
        
        
### Nvidia ###   
'nemotron-70b': nemotron_70b,


### Teknium ###   
'openhermes-2.5': openhermes_2_5,
        
        
### Pawan ###   
'cosmosrp': cosmosrp,


### Liquid ###   
'lfm-40b': lfm_40b,
      
        
### DiscoResearch ###   
'german-7b': german_7b,


### HuggingFaceH4 ###   
'zephyr-7b': zephyr_7b,
        
        
        
#############
### Image ###
#############
        
### Stability AI ###
'sdxl': sdxl,
'sdxl-lora': sdxl_lora,
'sdxl-turbo': sdxl_turbo,
'sd-1.5': sd_1_5,
'sd-3': sd_3,
        
        
### Playground ###
'playground-v2.5': playground_v2_5,


### Flux AI ###
'flux': flux,
'flux-pro': flux_pro,
'flux-realism': flux_realism,
'flux-anime': flux_anime,
'flux-3d': flux_3d,
'flux-disney': flux_disney,
'flux-pixel': flux_pixel,
'flux-4o': flux_4o,
'flux-schnell': flux_schnell,


### OpenAI ###
'dalle': dalle,
'dalle-2': dalle_2,

### Midjourney ###
'midjourney': midjourney,


### Other ###
'emi': emi,
'any-dark': any_dark,
    }

_all_models = list(ModelUtils.convert.keys())
