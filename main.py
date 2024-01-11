import os
from argparse import ArgumentParser, BooleanOptionalAction

from settings import Settings
from zipextracter import ZipExtracter
from compressor import ImageCompressor
from zipsaver import ZipSaver


def add_cli_args(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-p", "--path", required=True, help="Path to target docx file", type=str
    )
    parser.add_argument(
        "-r",
        "--replace",
        help="Replace target file to a compressed version instead of creating a new file",
        default=False,
        type=bool,
        action=BooleanOptionalAction,
    )
    parser.add_argument(
        "--postfix",
        help="Add a postfix to the output file",
        default="_compressed",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--ignore-less",
        help="Ignore files less than <value> (KB) in size",
        default=100,
        type=int,
    )


def parse_args_to_settings(parser: ArgumentParser) -> Settings:
    args = parser.parse_args()

    return Settings(
        path=args.path,
        should_replace=args.replace,
        postfix=args.postfix,
        ignore_less_than=args.ignore_less * 1024,
    )


def main() -> None:
    args_parser = ArgumentParser()

    add_cli_args(args_parser)

    settings = parse_args_to_settings(args_parser)

    zip_extracter = ZipExtracter(settings.path)
    zip_extracter.extract()

    image_folder_path = os.path.join(zip_extracter.get_extract_path(), "word", "media")

    compressor = ImageCompressor(
        image_folder_path, ignore_less_than=settings.ignore_less_than
    )
    compressor.compress()

    output_file_path = (
        settings.path if settings.should_replace else settings.path + settings.postfix
    )
    output_file_path = output_file_path.replace(".docx", "")

    zip_saver = ZipSaver(
        folder_path=zip_extracter.get_extract_path(),
        path_to_save=output_file_path,
        extension="docx",
    )
    zip_saver.save()

    zip_extracter.clear()


if __name__ == "__main__":
    main()
