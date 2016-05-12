var gulp = require('gulp');
var sass = require('gulp-sass');
var livereload = require('gulp-livereload');

gulp.task('sass', function () {
  gulp.src('sass/styles.sass')
    .pipe(sass())
    .pipe(gulp.dest('./dist'))
    .pipe(livereload());
});

gulp.task('watch', function () {
  livereload.listen({quite: true});
  gulp.watch(['./sass/**'], ['sass']);
  gulp.watch(['./copy/**'], ['copy']);
});

gulp.task('copy', function () {
  gulp.src([
    'node_modules/jquery/dist/jquery.min.js',
    'js/*'
  ]).pipe(gulp.dest('./dist/js'));

  gulp.src([
    'node_modules/font-awesome/fonts/*',
    'node_modules/open-sans-fontface/fonts/**/*'
  ]).pipe(gulp.dest('./dist/fonts'));

  gulp.src('img/**')
    .pipe(gulp.dest('./dist/img'));
});

gulp.task('build', ['copy', 'sass']);
gulp.task('default', ['build', 'watch']);
