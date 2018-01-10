# get all project files
file(GLOB_RECURSE ALL_SOURCE_FILES *.cpp *.c *.h *.m *.java)

find_program(GIT
	NAMES
	git)

find_program(CLANG_FORMAT
	NAMES
	clang-format
	clang-format-3.7
	clang-format-3.8
	clang-format-3.9
	clang-format-4.0
	clang-format-5.0
	clang-format-6.0)

add_custom_target(
        clangformat
        COMMAND ${CLANG_FORMAT}
        -style=file
        -i
        ${ALL_SOURCE_FILES}
)

