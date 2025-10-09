from loguru import logger
import sys

def chat(msg: str="Digite quais campos voce deseja extrair") -> str :
    try:
        text = input(msg).strip()
        if not text:
            logger.warning("Por favor insira alguma informacao que voce deseja extrair da Nf")
            return chat(msg)
        return text
    except (EOFError, KeyboardInterrupt):
        logger.info("\nEncerrado pelo usuário.")
        sys.exit(0)