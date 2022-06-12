from functools import lru_cache
import logging
from typing import Iterator

from devsearch.tree_sitter.setup import parser_library

logger = logging.getLogger(__name__)


@lru_cache(maxsize=None)
def get_identifiers_with_query(language: str, source_code: bytes) -> Iterator[str]:
    """
    This method returns all identifiers in given source_code via pattern matching
    Args:
        language: code language
        source_code: source code
    Returns: iterator of identifiers
    """

    try:
        parser = parser_library.get_parser(language)
        query = parser_library.get_language(language).query(
            """(
              (identifier) @constant
            )""")  # todo maybe specify identifier to any language

        captures = query.captures(parser.parse(source_code).root_node)
        for capture in captures:
            node = capture[0]
            ident = source_code[node.start_byte: node.end_byte].decode()
            yield ident
    except AttributeError:
        # if tree-sitter can not find the language
        logger.error(f"tree-sitter can't find parser for language: {language}")

# todo - languages identifiers names:
# js - identifier, property_identifier
# go - field_identifier, identifier, etc
