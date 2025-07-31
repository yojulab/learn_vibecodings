import { IsOptional, IsString, MaxLength } from 'class-validator';

export class UpdatePostDto {
  @IsString()
  @IsOptional()
  @MaxLength(255)
  title?: string;

  @IsString()
  @IsOptional()
  content?: string;
}
