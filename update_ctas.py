import re

file_path = r'c:\Users\Niko Movisk\low-ticket-glp\protocolo-glp1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero CTA
content = content.replace(
    'QUERO O PROTOCOLO AGORA',
    'SIM! QUERO ASSUMIR O CONTROLE DA MINHA ROTINA'
)

# 2. Bottom/FAQ CTA
content = content.replace(
    'QUERO GARANTIR MEU ACESSO AGORA',
    'SIM! QUERO DESTRAVAR MEUS RESULTADOS'
)

# 3. Basic Plan CTA
# The basic plan button has 'from-orange-400'
content = re.sub(
    r'(from-orange-400[^>]*>)\s*GARANTIR OFERTA AGORA!',
    r'\1\n              QUERO COMEÇAR PELO BÁSICO',
    content
)

# 4. Advanced Plan CTA
# The advanced plan button has 'from-green-500'
content = re.sub(
    r'(from-green-500[^>]*>)\s*GARANTIR OFERTA AGORA!',
    r'\1\n              QUERO O SISTEMA COMPLETO + BÔNUS',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('CTAs updated.')
